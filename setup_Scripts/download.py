import os
import json
import time
import requests
import settings
import pandas as pd
import tkinter as tk
from threading import *
from tkinter import ttk
from io import StringIO
from tkinter import messagebox as msg
from multiprocessing.pool import ThreadPool


# Configure progressbar
s = ttk.Style()

def get_data(server, folder, formsid, user, passw,keyfile, attach):

    # function to update abort value to break code
    def stop():
        global abort
        settings.abort = 1

    # loop through all formids and download
    #######################################
    num_files = 0
    for fid in formsid.split(','):

        start = time.time()  # Time running this year
        num_files += 1
        print("FormID:", fid, attach)
        # Progress Bar Widgets
        altbg1 = "#A0C7B2"
        tk.Label(settings.sel_frame, text="",bg=altbg1).grid(row=35, column=0, columnspan=2, ipady=2)
        pb = ttk.Progressbar(settings.sel_frame , orient='horizontal',mode='determinate', length=400 )
        action_label = tk.Label(settings.sel_frame, text="",bg=altbg1,fg="#110586",font=('Airial', 12, 'bold'))
        value_label = tk.Label(settings.sel_frame, text=f"Current Progress: 0.0%",fg="#110586",bg=altbg1,font=('Airial', 12, 'bold'))
        stop_butt = tk.Button(settings.sel_frame, text= "Cancel/Abort",width=20,  font=('Tahoma', 12), command=stop)
        pb['value'] = 0

        if not os.path.exists(folder + "/media"):
            os.makedirs(folder + "/media")

        # Connecting to server with a private key
        # ##################################
        if keyfile != '':
            files = {'private_key': open(keyfile, 'rb')}
            conn =requests.post(
                f'https://{server}.surveycto.com/api/v2/forms/data/wide/json/{fid}?date=0',
                files=files, auth=(user, passw))
            action_label['text'] = f"Downloading {fid} Data"
            dat = conn.json()
        # Connecting to server without private key
        # ##################################
        elif server != '':
            conn =requests.get(
                f'https://{server}.surveycto.com/api/v2/forms/data/wide/json/{fid}?date=0',
                auth=(user, passw))
            dat = conn.json()


        def get_missing(jdf):
            # Connect to API v1 to get missing fields
            url2 = f"https://{server}.surveycto.com/api/v1/forms/settings/csv/linebreak?v=%20"
            con = requests.post(url2, auth=(user, passw))
            url3 = f"https://{server}.surveycto.com/api/v1/forms/data/wide/csv/{formsid}"
            data = requests.get(url3, auth=(user, passw))
            dt = data.text
            csv_donw = pd.read_csv(StringIO(dt))
            cols = csv_donw.columns
            # Loop through columns and get missing values
            for j in cols:
                if j not in jdf.columns:
                    try:
                        jdf[j] = csv_donw[j]
                    except:
                        jdf[j] = ""
            try:
                # Rearrange index
                outcols = ["instanceID", "formdef_version", "KEY"]
                cols = jdf.columns.to_list()
                cols = [ele for ele in cols if ele not in outcols]
                new_cols = cols + outcols
                jdf = jdf.reindex(columns=new_cols)
            except:
                pass
            jdf.to_csv(f"{folder}/{fid}.csv", index=False)
            value_label['text'] = f"Current Progress: 100%"
            pb['value'] = 100


        # Function for download
        def d_data_key():

            action_label['text'] = f"Downloading {fid} Data"
            attach_links = []
            action_label.grid_remove()
            action_label['text'] = f"Downloading {fid} Data"
            action_label.grid(row=38, column=0, columnspan=2)

            fdf = pd.DataFrame(dat)
            # fdf = pd.read_json(json.dumps(dat))

            # Get attachment links
            ds = fdf.stack()
            attach_links = list(ds[ds.str.contains('surveycto.com/')])
            print(attach_links)
            p_len = len(attach_links)

            # rename fields with attachements by removing links
            # And also ordering columns
            try:
                fdf.replace(r"^http.*?/attachments/", 'media/', inplace=True, regex=True)
                fdf = fdf.drop(columns="CompletionDate")
                # Move some columns to the end
            except:
                pass

            # try getting missing data
            get_missing(fdf)

            # Getting Attachments
            #####################
            if attach == "Yes":
                # Download called in a thread
                action_label.grid_remove()
                stop_butt.grid_remove()
                action_label['text'] = f"Downloading {fid} Attachments"
                action_label.grid(row=35, column=0, columnspan=2)
                stop_butt.grid(row=38, column=0, columnspan=2, pady=2)

                pb['value'] = 0
                # Download attachments
                settings.curr_att =0
                def download_url(url):
                    # Update progress bar and other widgets
                    settings.curr_att +=1
                    updated = round(int((settings.curr_att/p_len)*100))
                    pb['value']  = updated
                    settings.sel_frame.update_idletasks()
                    value_label['text'] = f"Current Progress: {updated}% ({settings.curr_att}/{p_len})"
                    time.sleep(0.5)  # Sleep time for threading

                    # Download with multi-processing
                    file_name = f'{folder}/media/' + url.split('/')[-1]
                    print("downloading: ", url, "to\n", file_name )
                    r = requests.get(url,auth=(user,passw), stream=True)
                    with open(file_name, 'wb') as f:
                        for data in r:
                            f.write(data)
                    return url

                # Run 100 multiple threads. Each call will take the next element in urls list
                urls = attach_links
                results = ThreadPool(100).imap_unordered(download_url, urls)
                for r in results:
                    print(r)
                    if settings.abort == 1:
                        msg.showinfo("Aborted", f"Download aborted by user at {round(pb['value'], 2)}%")
                        value_label.grid_remove()
                        action_label.grid_remove()
                        break

        # threading functions to avoid not responding
        def d_threadingkey():
            # Call work function
            dat = conn.json()
            t1 = Thread(target=d_data_key)
            t1.start()
        # Connection success
        if conn.status_code ==200:
            # Initiate widgets
            action_label['text'] = f"Downloading {fid} Data "
            value_label.grid(row=36, column=0, columnspan=2)
            action_label.grid(row=35, column=0, columnspan=2)
            pb.grid(row=37, column=0, columnspan=2)
            # Run thread
            d_threadingkey()
            settings.wait_time = time.time() -  start
        elif conn.status_code ==401:
            msg.showinfo("Invalid credentials",
                         "Server credentials not correct \n correct your login details and forms ID")
        elif conn.status_code ==417:
            msg.showinfo("Server Delay required",
                         f"SurveyCTO requires a minimum wait time of 300 to perform another call on {server} server \n \n "
                         f"minimum wait time remaining is {round(300-settings.wait_time)}")
        else:
            msg.showinfo("Connection Error",
                         "Unable to establish connection \nCheck your internet and try again")
