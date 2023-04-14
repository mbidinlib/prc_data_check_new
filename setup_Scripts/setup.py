# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose:
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
# -------------------------------------

import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import imoji
from datetime import date

import pandas as pd
from tkhtmlview import HTMLLabel
from tkinter import messagebox as msg
from PIL import Image, ImageTk

# call other Scripts
import settings
settings.gloSettings()
import create_folders
import dialogs
import gen_dictionaries
import checks_duplicate
import checks_missing
import checks_outliers
import checks_boundary
import checks_other_specify
import session_control

# Call Tk only from __main__
if __name__ == "__main__":
    # Tk root
    root = Tk()  # create root window
    root.config(bg="skyblue")
    root.geometry("950x650")

    # Change Notebook Style
    style = ttk.Style()
    coldef = "#DCF0F2"
    colsel = "skyblue2"
    mainbg = '#8AD19D'
    textcol1 = "#110586"
    textcol2 = "#7AB3F7"
    altbg2 = "#E3FBEE"
    altbg1 = "#A0C7B2"

    style.configure("TNotebook", background = mainbg)
    style.configure("TProgressbar", foreground='green', background='green')

    # Define tabs
    tabs = ttk.Notebook(root)
    setup_tab = ttk.Frame(tabs)
    checks_tab = ttk.Frame(tabs)
    tabs.add(setup_tab, text="Setup")
    tabs.add(checks_tab, text="Data Checks")
    tabs.pack(expand=1, fill=BOTH)
    # root.configure(bg=mainbg)
    # Header
    # logo = Image.open("C:/Mine/PRC_Logo/PRC.png").resize((45, 30))
    # img = ImageTk.PhotoImage(logo)
    # sup_header= Label(setup_tab, image = img,fg=textcol1,bg=mainbg,
    #                  font=('Arial Black', 20,'bold')).place( x=1, y=1)
    sup_header = Label(setup_tab, text="  PRC DATA CHECK SOLUTION", fg=textcol1, bg=mainbg,
                       font=('Arial Black', 20, 'bold')).pack(fill=X)

    # Setup tab
    #############
    # Frame 1
    sel_frame = Frame(setup_tab, bg=altbg1)
    sel_frame.pack(side=LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    Label(sel_frame, text="", font=('Airial', 14), bg=altbg1).grid(row=0, column=0, columnspan=3, pady=20,
                                                                   padx=10)  # Empty lable to give line space
    sup_details = Label(sel_frame, text="Setup Folder Structure", bg=altbg1, \
                        font=('Airial', 17, "bold", "underline")).grid(row=1, column=0, columnspan=3, padx=10, pady=5)
    Label(sel_frame, text="", font=('Airial', 14), bg=altbg1).grid(row=8, column=0, columnspan=3, pady=2,
                                                                   padx=1)  # Empty lable to give line space


    # Functione to select folder
    def sel_pfolder():
        global f_dir
        dialogs.get_folder()
        pa_folder.delete(0, END)
        pa_folder.insert(0, settings.folder_name)
        root.update()


    # Location of folders
    folder_loc_lab = Label(sel_frame, text="Enter or select location for folders", font=('Airial', 14), bg=altbg1)
    folder_loc_lab.grid(row=10, column=0, columnspan=3, pady=1, padx=10)
    folder_loc = tk.StringVar()
    pa_folder = Entry(sel_frame, width=30, font=('Airial', 12), textvariable=folder_loc)
    pa_folder.grid(row=17, column=0, padx=4, ipady=7)
    pfolder_sel = Button(sel_frame, text='Select location', font=('Tahoma', 12), height=1, width=16,
                         command=sel_pfolder)
    pfolder_sel.grid(row=17, column=1)


    def start_folder_creation():
        settings.parent_folder = folder_loc.get()  # Get the in
        create_folders.start()


    # Button to create folder structure
    Label(sel_frame, text="", font=('Airial', 14), bg=altbg1).grid(row=18, column=0, columnspan=3,
                                                                   padx=10)  # Empty label widget
    setup_folders = Button(sel_frame, text='Create Folders', font=('Tahoma', 11), height=2, width=30, bg='skyblue1',
                           command=start_folder_creation).grid(row=19, column=0, columnspan=2)

    # Setup Frame 2 :
    # Generate Dictionaries and prepare data
    #########################################
    dict_frame = Frame(setup_tab, width=920, bg=altbg2)
    dict_frame.pack(side=RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
    settings.dict_frame = dict_frame

    dic_hedder = Label(dict_frame, text="Create Data Dictionaries", bg=altbg2, \
                       font=('Airial', 20, "bold", "underline")).grid(row=1, column=1, columnspan=4, padx=10, pady=10)

    # Apply Dictionary to categorical data
    Label(dict_frame, text="Apply to data", bg=altbg2, \
          font=('Airial', 12)).grid(row=2, column=3, sticky=E)
    apply_items = ("Yes", "No")
    apply_val = tk.StringVar(dict_frame)
    apply_val.set("Yes")
    app_files = tk.OptionMenu(dict_frame, apply_val, *apply_items)
    app_files.grid(row=2, column=4, ipady=2, sticky=W)  # E
    apply_to_data = apply_val.get()


    def call_dialogs(fname):
        fname = fname
        settings.parent_folder = folder_loc.get()  # Get the in
        dialogs.get_file(fname)
        # Evaluate the file button clicked and inset name of file in the entry field
        ent_selected = eval("settings." + fname[0] + "_file" + fname[-1] + "_ent")  # Evaluate the field to populate

        eval(fname[0] + "_file" + fname[-1] + "_ent").delete(0, END)
        eval(fname[0] + "_file" + fname[-1] + "_ent").insert(0, eval(
            "settings." + fname[0] + "_file" + fname[-1] + "_ent"))


    Label(dict_frame, text="", font=('Airial', 14), bg=altbg2).grid(row=10, column=1, ipady=2)  # Empty label widget
    # Column Heads:
    Label(dict_frame, text="xls Form", font=('Airial', 12, "underline"), bg=altbg2).grid(row=16, column=1, columnspan=2)
    Label(dict_frame, text="Raw  Data", font=('Airial', 12, "underline"), bg=altbg2).grid(row=16, column=3,
                                                                                          columnspan=1, sticky=E)

    # Selecting Data File 1
    file1_lab = Label(dict_frame, text="1:", font=('Airial', 12), bg=altbg2)
    x_file1_note_n = tk.StringVar()
    x_file1_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=x_file1_note_n)
    d_file1_note_n = tk.StringVar()
    d_file1_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=d_file1_note_n)
    r_xfile1_sel = Button(dict_frame, text='Select xls file', font=('Tahoma', 12), width=12,
                          command=lambda fname="xfile1": call_dialogs(fname))
    r_dfile1_sel = Button(dict_frame, text='select raw data', font=('Tahoma', 12), width=12,
                          command=lambda fname="dfile1": call_dialogs(fname))

    # Selecting Data File 2
    Label(dict_frame, text="", font=('Airial', 4), bg=altbg2).grid(row=18, column=0)  # Empty label widget
    file2_lab = Label(dict_frame, text="2:", font=('Airial', 12), bg=altbg2)
    x_file2_note_n = tk.StringVar()
    x_file2_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=x_file2_note_n)
    d_file2_note_n = tk.StringVar()
    d_file2_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=d_file2_note_n)

    r_xfile2_sel = Button(dict_frame, text='select xls file', font=('Tahoma', 12), width=12,
                          command=lambda fname="xfile2": call_dialogs(fname))
    r_dfile2_sel = Button(dict_frame, text='select raw data', font=('Tahoma', 12), width=12,
                          command=lambda fname="dfile2": call_dialogs(fname))

    # Selecting Data File 3
    Label(dict_frame, text="", font=('Airial', 4), bg=altbg2).grid(row=20, column=0)  # Empty label widget
    file3_lab = Label(dict_frame, text="3:", font=('Airial', 12), bg=altbg2)
    x_file3_note_n = tk.StringVar()
    x_file3_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=x_file3_note_n)
    d_file3_note_n = tk.StringVar()
    d_file3_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=d_file3_note_n)

    r_xfile3_sel = Button(dict_frame, text='select xls file', font=('Tahoma', 12), height=1, width=12,
                          command=lambda fname="xfile3": call_dialogs(fname))
    r_dfile3_sel = Button(dict_frame, text='select raw data', font=('Tahoma', 12), height=1, width=12,
                          command=lambda fname="dfile3": call_dialogs(fname))

    # Selecting Data File 4
    Label(dict_frame, text="", font=('Airial', 4), bg=altbg2).grid(row=22, column=0)  # Empty label widget
    file4_lab = Label(dict_frame, text="4:", font=('Airial', 12), bg=altbg2)
    x_file4_note_n = tk.StringVar()
    x_file4_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=x_file4_note_n)
    d_file4_note_n = tk.StringVar()
    d_file4_ent = Entry(dict_frame, width=15, font=('Airial', 9), textvariable=d_file4_note_n)

    r_xfile4_sel = Button(dict_frame, text='select xls file', font=('Tahoma', 12), height=1, width=12,
                          command=lambda fname="xfile4": call_dialogs(fname))
    r_dfile4_sel = Button(dict_frame, text='select raw data', font=('Tahoma', 12), height=1, width=12,
                          command=lambda fname="dfile4": call_dialogs(fname))

    # Selecting Data File 5
    Label(dict_frame, text="", font=('Airial', 4), bg=altbg2).grid(row=24, column=0)  # Empty label widget
    file5_lab = Label(dict_frame, text="5:", font=('Airial', 12), bg=altbg2)
    x_file5_note_n = tk.StringVar()
    x_file5_ent = Entry(dict_frame, width=15, font=('Airial', 10), textvariable=x_file5_note_n)
    d_file5_note_n = tk.StringVar()
    d_file5_ent = Entry(dict_frame, width=15, font=('Airial', 10), textvariable=d_file5_note_n)

    r_xfile5_sel = Button(dict_frame, text='select xls file', font=('Tahoma', 12), height=1, width=12,
                          command=lambda fname="xfile5": call_dialogs(fname))
    r_dfile5_sel = Button(dict_frame, text='select raw data', font=('Tahoma', 12), height=1, width=12,
                          command=lambda fname="dfile5": call_dialogs(fname))

    # placing each row in grid view
    ###############################

    # Place Selecting Data File 1
    file1_lab.grid(row=17, column=0, sticky=W)
    r_xfile1_sel.grid(row=17, column=1, sticky=E)
    x_file1_ent.grid(row=17, column=2, ipady=6, padx=10)
    r_dfile1_sel.grid(row=17, column=3, padx=30, sticky=E)
    d_file1_ent.grid(row=17, column=4, ipady=6, sticky=E)


    # Callback function to update number of files
    # ###########################################
    def update_file_number(num_raw_file):
        num_raw_file = num_files_val.get()
        settings.num_raw_files = num_files_val.get()
        # Place Selecting Data File 2

        if num_raw_file >= 2:
            file2_lab.grid(row=19, column=0, sticky=W)
            r_xfile2_sel.grid(row=19, column=1, sticky=E)
            x_file2_ent.grid(row=19, column=2, ipady=6, padx=10)
            r_dfile2_sel.grid(row=19, column=3, padx=30, sticky=E)
            d_file2_ent.grid(row=19, column=4, ipady=6, sticky=E)
        elif num_raw_file < 2:
            file2_lab.grid_remove()
            x_file2_ent.grid_remove()
            d_file2_ent.grid_remove()
            r_xfile2_sel.grid_remove()
            r_dfile2_sel.grid_remove()

        # Place Selecting Data File 3
        if num_raw_file >= 3:
            file3_lab.grid(row=21, column=0, sticky=W)
            r_xfile3_sel.grid(row=21, column=1, sticky=E)
            x_file3_ent.grid(row=21, column=2, ipady=6, padx=10)
            r_dfile3_sel.grid(row=21, column=3, padx=30, sticky=E)
            d_file3_ent.grid(row=21, column=4, ipady=6, sticky=E)
        elif num_raw_file < 3:
            file3_lab.grid_remove()
            x_file3_ent.grid_remove()
            d_file3_ent.grid_remove()
            r_xfile3_sel.grid_remove()
            r_dfile3_sel.grid_remove()

        # Place Selecting Data File 4
        if num_raw_file >= 4:
            file4_lab.grid(row=23, column=0, sticky=W)
            r_xfile4_sel.grid(row=23, column=1, sticky=E)
            x_file4_ent.grid(row=23, column=2, ipady=6, padx=10)
            r_dfile4_sel.grid(row=23, column=3, padx=30, sticky=E)
            d_file4_ent.grid(row=23, column=4, ipady=6, sticky=E)
        elif num_raw_file < 4:
            file4_lab.grid_remove()
            x_file4_ent.grid_remove()
            d_file4_ent.grid_remove()
            r_xfile4_sel.grid_remove()
            r_dfile4_sel.grid_remove()
        # Place Selecting Data File 5
        if num_raw_file >= 5:
            file5_lab.grid(row=25, column=0, sticky=W)
            r_xfile5_sel.grid(row=25, column=1, sticky=E)
            x_file5_ent.grid(row=25, column=2, ipady=6, padx=10)
            r_dfile5_sel.grid(row=25, column=3, padx=30, sticky=E)
            d_file5_ent.grid(row=25, column=4, ipady=6, sticky=E)
        elif num_raw_file < 5:
            file5_lab.grid_remove()
            x_file5_ent.grid_remove()
            d_file5_ent.grid_remove()
            r_xfile5_sel.grid_remove()
            r_dfile5_sel.grid_remove()
        # msg.showinfo("GG", num_raw_file)
        root.update()


    # Select Number of Data files
    Label(dict_frame, text="Number of files", bg=altbg2, \
          font=('Airial', 11)).grid(row=2, column=1, pady=10, sticky=W)
    num_file_items = ("1", "2", "3", "4", "5")
    num_files_val = tk.IntVar(dict_frame)
    num_files_val.set("1")
    num_d_files = tk.OptionMenu(dict_frame, num_files_val, *num_file_items, command=update_file_number)
    num_d_files.grid(row=2, column=2, ipady=5, sticky=W)  # E



    def sel_parent_folder():
        dialogs.get_folder()
        p_folder.delete(0, END)
        p_folder.insert(0, settings.folder_name)
        settings.parent_folder = settings.folder_name
        root.update()

    # Location of Dictionary folder
    p_folder_sel = Button(dict_frame, text='Select Parent folder', font=('Airial', 12), height=2, width=25,
                          bg='skyblue1', command=sel_parent_folder)
    p_folder_sel.grid(row=28, column=1, columnspan=2, sticky=W)
    Label(dict_frame, text="", font=('Airial', 12), bg=altbg2).grid(row=29, column=1, pady=1)

    # Display location in anEntry field
    p_folder_lab = Label(dict_frame, text="Parent Folder Path", font=('Airial', 12), bg=altbg2)
    p_folder_lab.grid(row=30, column=1, columnspan=4, pady=1, padx=10)
    p_folder_loc = tk.StringVar()
    p_folder = Entry(dict_frame, width=56, font=('Airial', 9), textvariable=p_folder_loc)
    p_folder.grid(row=31, column=1, padx=4, ipady=3, columnspan=4)


    # Functions to create dictionary
    # ###############################
    def create_dictionaries():
        settings.num_raw_files = num_files_val.get()
        settings.main_folder = p_folder_loc.get()  # Get the in

        if (settings.raw_file1 == "" and settings.raw_file2 == "" and settings.raw_file3 == "" and settings.raw_file4 ==
                "" and settings.raw_file5 == ""):

            msg.showinfo("No File Selected", "Select a valid xls file")

        elif settings.main_folder == "":
            msg.showinfo("No Folder Selected", "Select the Parent folder or enter full location")

        else:
            gen_dictionaries.gen_dict_files()

    # Button to Generate Dictionaries
    # ###############################
    Label(dict_frame, text="", font=('Airial', 14), bg=altbg2).grid(row=26, column=0, columnspan=3,
                                                                    ipady=1)  # Empty label widget
    gen_diction = Button(dict_frame, text='Generate Dictionaries', font=('Airial', 11), height=2, width=26,
                         bg='skyblue2', command=create_dictionaries).grid(row=28, column=2, columnspan=3, sticky=E)


    ###############################################################
    # ################### API Data Download #######################
    ###############################################################
    Label(sel_frame, text="", font=('Airial', 14), bg=altbg1).grid(row=20, column=0, columnspan=3, pady=9,)
    api_lab = Label(sel_frame, text="API Data Download", bg=altbg1, font=('Airial', 16, "bold", "underline"))
    api_lab.grid(row=23, column=0, columnspan=2, sticky=NSEW)

    # Call back function for API buttons and Combo
    # ###########################################
    def api_callback(action,value):
        # Selecting folder
        if action == 'folder':
            dialogs.get_folder()
            value.delete(0,END)
            value.insert(END,settings.folder_name)
        # Selecting key file
        if action == 'file':
            dialogs.get_file("dfile")
            value.delete(0, END)
            value.insert(END, settings.fname)
        # For Type selection
        if action == 'type':

            # SurveyCTO
            if value == "SurveyCTO":
                print("SCTO")
                cto_server_lab.grid(row=27, column=0, sticky=W)
                cto_server.grid(row=27, column=0, columnspan=2, pady=2, ipady=2)
                cto_user_lab.grid(row=28, column=0, sticky=W)
                cto_user.grid(row=28, column=0, columnspan=2, pady=2, ipady=2)
                cto_pass_lab.grid(row=29, column=0, sticky=W)
                cto_pass.grid(row=29, column=0, columnspan=2, pady=2, ipady=2)
                cto_forms_lab.grid(row=30, column=0, sticky=W)
                cto_forms.grid(row=30, column=0, columnspan=2, pady=2, ipady=2)
                cto_attach_lab.grid(row=31, column=0,sticky=W)
                cto_attach_butt.grid(row=31, column=0,ipady=2)
                cto_sel_file.grid(row=27, column=1, ipady=2,sticky=E)
                cto_key.grid(row=28, column=1, ipady=2,sticky=E)
                cto_loc.grid(row=30, column=1, ipady=2,sticky=E)
                cto_loc_but.grid(row=29, column=1, ipady=2,sticky=E)
                cto_run.grid(row=31, column=0,columnspan=2,sticky=E)
            # Remove all widgets
            elif value == '':
                cto_server_lab.grid_remove()
                cto_server.grid_remove()
                cto_user_lab.grid_remove()
                cto_user.grid_remove()
                cto_pass_lab.grid_remove()
                cto_pass.grid_remove()
                cto_forms_lab.grid_remove()
                cto_forms.grid_remove()
                cto_attach_butt.grid_remove()
                cto_sel_file.grid_remove()
                cto_loc.grid_remove()
                cto_attach_lab.grid_remove()
                cto_key.grid_remove()
                cto_loc_but.grid_remove()
                cto_run.grid_remove()
    # General Widgets
    api_type_opts = ("", "SurveyCTO", "ONA Collect", "ODK", "Qualtrics")
    api_type_butt = ttk.Combobox(sel_frame, values=api_type_opts, width=25)
    api_type_butt.bind('<<ComboboxSelected>>', lambda event,action ='type', option=api_type_butt: api_callback(action, option.get()))  # callback function when combobox changes
    api_type_butt.set(" Select Platform")
    api_type_butt.grid(row=25, column=0, columnspan=2, pady=2, ipady=2)

    # SCTO Widgets
    # ###########
    import download
    cto_server_lab = Label(sel_frame, text="  Enter server name", font=('Airial', 9), bg=altbg1)
    cto_server = ttk.Entry(sel_frame, width=25)
    cto_user_lab = Label(sel_frame, text="    Login username", font=('Airial', 9), bg=altbg1)
    cto_user = ttk.Entry(sel_frame, width=25)
    cto_pass_lab = Label(sel_frame, text="   Login  Password", font=('Airial', 9), bg=altbg1)
    cto_pass = ttk.Entry(sel_frame,show="*" ,width=25)
    cto_forms_lab = Label(sel_frame, text="   Enter Form IDs", font=('Airial', 9), bg=altbg1)
    cto_forms = ttk.Entry(sel_frame, width=25)
    cto_attach_lab = Label(sel_frame, text="  Get Attachments", font=('Airial', 9), bg=altbg1)
    cto_attach_butt = ttk.Combobox(sel_frame, values=("Yes", "No"), width=9)
    cto_attach_butt.set("Yes")
    cto_key = ttk.Entry(sel_frame, width=19)
    cto_sel_file = Button(sel_frame, text='Select Key File', font=('Tahoma', 12),  width=12,
                           command= lambda val = cto_key, action = 'file': api_callback(action, val))
    cto_loc = ttk.Entry(sel_frame, width=19)
    cto_loc_but = Button(sel_frame, text='Data Location', font=('Tahoma', 12),  width=12,
                           command= lambda val = cto_loc, action = 'folder': api_callback(action, val))

    def run_data_download():
        settings.sel_frame = sel_frame
        if cto_server.get() == '':
            msg.showerror("Entry Error", "Enter Server Name")
        elif cto_user.get() == '':
            msg.showerror("Entry Error", "Enter User Name")
        elif cto_pass.get() == '':
            msg.showerror("Entry Error", "Enter Password")
        elif cto_forms.get() == '':
            msg.showerror("Entry Error", "Enter Valid ID of forms seperated by a comma")
        elif cto_loc.get() == '':
            msg.showerror("Entry Error", "Select Valid location of Data")
        else:
            download.get_data(cto_server.get(), cto_loc.get(), cto_forms.get(), cto_user.get(),
                              cto_pass.get(), cto_key.get(), cto_attach_butt.get())

    cto_run = Button(sel_frame, text='Download', font=('Tahoma', 12),  width=24, bg='skyblue1',
                command=run_data_download)









    # ########################################################################################
    #                                   2 Checks tab
    #                       Define and place all widgets in the checks tab
    # #########################################################################################

    # BG Colors fo check regions
    checksbg1 = "#73C6B6"
    checksbg2 = "#7DCEA0"
    checksbg3 = "#82E0AA"
    checksbg4 = "#2ECC71"
    checksbg5 = "#229954"
    checksbg6 = "#138D75"
    checkssetbg = "#D1F2EB"

    # BG Colors fo check colums
    datacol1 = '#76448A'
    datacol2 = '#B03A2E'

    datacol3 = '#2874A6'
    datacol4 = '#B9770E'
    datacol5 = '#D98880'
    white = '#FFFFFF'


    # Parent PanedWindow
    panedwin1 = PanedWindow(checks_tab, sashwidth=15, sashrelief="raised", bd=5)
    panedwin1.pack(expand=True, fill='both')
    checks_set_frame = Frame(panedwin1, width=400, bg=checkssetbg, relief=SUNKEN)
    # checks_set_frame = Scrollbar(panedwin1, orient='horizontal')
    panedwin1.add(checks_set_frame)

    # Add Child Pane (Use add method)
    panedwin2 = PanedWindow(panedwin1, sashwidth=15, sashrelief="raised", bd=5)
    panedwin1.add(panedwin2)

    # Divide the second pane into two section for further patition
    ##############################################################
    # Partition 1: Top three
    checkspart1 = PanedWindow(panedwin2, sashwidth=15, sashrelief="raised")
    checkspart1.pack(expand=True, fill='both', side=TOP)
    checks_frame1 = Frame(checkspart1, bg=checksbg1, bd=10)
    checks_frame3 = Frame(checkspart1, bg=checksbg3, bd=10)
    checks_frame2 = Frame(checkspart1, bg=checksbg2, bd=10)
    checkspart1.add(checks_frame1)
    checkspart1.add(checks_frame2)
    checkspart1.add(checks_frame3)

    # Partition 2: Bottom three
    checkspart2 = PanedWindow(panedwin2, sashwidth=15, sashrelief="raised")
    checkspart2.pack(expand=True, fill='both', side=BOTTOM)
    # Children of the bottom partition
    checks_frame4 = Frame(checkspart2, bg=checksbg4, bd=10)
    checks_frame6 = Frame(checkspart2, bg=checksbg6, bd=10)
    checks_frame5 = Frame(checkspart2, bg=checksbg5, bd=10)
    checkspart2.add(checks_frame4)
    checkspart2.add(checks_frame5)
    checkspart2.add(checks_frame6)

    # Populate the Frames
    #####################

    ###################
    # 1. Settings Frame
    # #################
    Label(checks_set_frame, text="Settings", bg=checkssetbg,
          font=('Airial', 20, "bold")).grid(row=0, columnspan=4, padx=5, column=1, sticky=NSEW)


    # Function to call number of datafiles
    ######################################
    def update_check_number(n_d_files):
        num_data_file = num_data_val.get()
        settings.num_data_files = num_data_val.get()

        # For Session Restoration
        if int(n_d_files) > 0:
            nf= int(n_d_files)
        # For main widget update
        else:
            nf = num_data_file

        # Loop through the number of files selected
        for k in range(nf):
            k = k + 1
            rw = k * 4
            # Place the elements on the settings pad based on the number selectred
            # Default widget
            exec(f"check_raw{k}_sel.grid(row= {rw} , column=1)")  # Places each of the buttons that selects the raw data
            exec(f"c_lab{k}.grid(row= {rw}, rowspan=3, column=0, sticky=E)")
            exec(f"check_raw{k}_ent.grid(row=  {rw + 1} , column=1)")
            exec(f"c_space{k}.grid(row={(k * 4) + 3}, column=0, padx=1)")

            # Widget that may be present
            if eval(f"settings.check_raw{k} !='' "):
                exec(f"settings.checks_id{k}.grid(row={k * 4}, column=3,ipady=3)")
                exec(f"settings.id_ent{k}.grid(row={k * 4 + 1}, column=3)")
                exec(f"settings.keep_ent{k}.grid(row={k * 4 + 1}, column=5)")
                exec(f"settings.keepsel{k}.grid(row={k * 4}, column=5,ipady=3)")
                exec(f"settings.dp{k}.grid(row={k*2 + 26}, column=3, sticky=W, pady=2)")
                exec(f"settings.ms{k}.grid(row={k*2  + 26}, column=3,  pady=2)")
                exec(f"settings.ol{k}.grid(row={k*2  + 26}, column=3, sticky=E, pady=2)")
                exec(f"settings.ot{k}.grid(row={k*2  + 26}, column=5, sticky=W, pady=2)")
                exec(f"settings.bo{k}.grid(row={k*2  + 26}, column=5,  pady=2)")
                exec(f"settings.tb{k}.grid(row={k*2  + 26}, column=5, sticky=E, pady=2)")
                exec(f"settings.ckb{k}.grid(row={k*2 + 26}, column = 1, sticky = 'NSEW') ")

        # Forget those on rows more than the selected number
        if nf < 5:
            for k in range(nf, 5, 1):
                k = k + 1
                # Remove default widgets
                exec(f"check_raw{k}_sel.grid_forget()")  # Places each of the buttons that selects the raw data
                exec(f"c_lab{k}.grid_forget()")
                exec(f"check_raw{k}_ent.grid_forget()")
                exec(f"c_space{k}.grid_forget()")

                # Other widgets that may not be present
                try:
                    exec(f"settings.checks_id{k}.grid_forget()")  # Remove redundant widgets for ID selection
                    exec(f"settings.ckb{k}.grid_forget()")  # Remove redundant check data checkbox widgets at the botton of the settings
                    exec(f"settings.dp{k}.grid_forget()")
                    exec(f"settings.ms{k}.grid_forget()")
                    exec(f"settings.ol{k}.grid_forget()")
                    exec(f"settings.ot{k}.grid_forget()")
                    exec(f"settings.bo{k}.grid_forget()")
                    exec(f"settings.tb{k}.grid_forget()")
                    exec(f"settings.checks_id{k}.grid_forget()")
                    exec(f"settings.id_ent{k}.grid_forget()")
                    exec(f"settings.keep_ent{k}.grid_forget()")
                    exec(f"settings.keepsel{k}.grid_forget()")

                except:
                    pass

        root.update()


    # Widgets for Selecting Number of Data files at the top
    #######################################################

    Label(checks_set_frame, text="Number of data", bg=checkssetbg, \
          font=('Airial', 12)).grid(row=2, column=1, pady=7, sticky=E)
    num_data_items = ("1", "2", "3", "4", "5")
    num_data_val = tk.IntVar(dict_frame)
    num_data_val.set("1")
    num_dta_files = tk.OptionMenu(checks_set_frame, num_data_val, *num_data_items, command=update_check_number)
    num_dta_files.grid(row=2, column=2, ipady=2, sticky=W)  # E
    Label(checks_set_frame, text="Raw Data", bg=checkssetbg, font=('Airial', 12,'underline')).grid(row=3, column=1, pady=2)
    Label(checks_set_frame, text="ID Variable", bg=checkssetbg, font=('Airial', 12,'underline')).grid(row=3, column=3, pady=2)
    Label(checks_set_frame, text="Check Keep", bg=checkssetbg, font=('Airial', 12,'underline')).grid(row=3, column=5, pady=2)

    # Define Integer-vars for check-buttons
    # ####################################
    for i in range(1, 6):
        fnum = i
        # Check box for each data
        exec(f"settings.run{fnum} = tk.IntVar()")
        # Individual checkbox vars for each check
        exec(f"settings.dup{fnum} = tk.IntVar()")
        exec(f"settings.miss{fnum} = tk.IntVar()")
        exec(f"settings.outl{fnum} = tk.IntVar()")
        exec(f"settings.other{fnum} = tk.IntVar()")
        exec(f"settings.bound{fnum} = tk.IntVar()")
        exec(f"settings.tabu{fnum} = tk.IntVar()")


    # Callback function to enable checks to be selected
    ###################################################
    def enable_checks(fnum):

        if eval(f"settings.run{fnum}.get()") == 1:  # if it is checked
            exec(f"settings.dp{fnum}.config(state='normal')")
            exec(f"settings.ms{fnum}.config(state='normal')")
            exec(f"settings.ol{fnum}.config(state='normal')")
            exec(f"settings.ot{fnum}.config(state='normal')")
            exec(f"settings.bo{fnum}.config(state='normal')")
            exec(f"settings.tb{fnum}.config(state='normal')")

        else:  # if it is checked
            exec(f"settings.dp{fnum}.config(state='disabled')")
            exec(f"settings.ms{fnum}.config(state='disabled')")
            exec(f"settings.ol{fnum}.config(state='disabled')")
            exec(f"settings.ot{fnum}.config(state='disabled')")
            exec(f"settings.bo{fnum}.config(state='disabled')")
            exec(f"settings.tb{fnum}.config(state='disabled')")


    # callback function when duplicates combobox changes
    # Used for selection of vars-to-keep, dup-id
    ###################################################
    def combo_callback(selected, num, name):
        if name == 'id_ent' or name == 'dup_id_ent' or name == 'keep_ent':
            val_ent = eval(f"settings.{name}{num}.get()")
        # Multiple selections
        if name == 'dup_id_ent' or name == 'keep_ent':
            if (val_ent == ''):  # If there's nothing in, don't add preceeding comma
                exec(f"settings.{name}{num}.insert(END, selected)")
            else:
                exec(f"settings.{name}{num}.insert(END, ',' + selected)")
        # Single selections
        elif name =='id_ent':
            if (val_ent == ''):  # If there's nothing in, don't add preceeding comma
                exec(f"settings.{name}{num}.insert(0, selected)")
            else:
                exec(f"settings.{name}{num}.delete(0,END)")
                exec(f"settings.{name}{num}.insert(END,selected)")
        elif name == 'miss_id_ent' or name == 'outl_id_ent':
            exec(f"settings.{name}{num}.insert(1.0, selected + ',\\n')")
        elif name == 'other_id_ent':
            fulltxt = eval(f"settings.{name}{num}.get(1.0, END)")
            p_var = eval("selected.split('|')[0]")
            c_var = eval("selected.split('|')[1]")
            # Check if both parent variables are selected
            if p_var == '':
                msg.showinfo("Variable Error", "No Parent variable selected")
            elif c_var == '':
                msg.showinfo("Variable Error", "No Child variable selected")
            else:
                exec(f"settings.{name}{num}.insert(1.0, selected + ',\\n')")
        elif name == 'bound_id_ent':
            fulltxt = eval(f"settings.{name}{num}.get(1.0, END)")
            m_var = eval("selected.split('|')[0]")
            l_var = eval("selected.split('|')[1]")
            u_var = eval("selected.split('|')[2]")
            # Check if both parent variables are selected
            if m_var == '':
                msg.showinfo("Variable Error", "No variable selected")
            elif l_var == '' and u_var == '':
                msg.showinfo("Variable Error", "At least one entry required for lower and upper bounds")
            else:
                exec(f"settings.{name}{num}.insert(1.0, selected + ',\\n')")


    # Function that selects and imports data
    # Select input file
    # #########################################
    selected_files = []
    def sel_file(fname):
        fnum = fname[-1]
        fn = int(fnum)

        # Ignore Restore trrigger and select files for the others
        if "Restore" not in fname:
            dialogs.get_file(fname)
            eval("check_raw" + fnum + "_ent").delete(0, END)
            eval("check_raw" + fnum + "_ent").insert(0, settings.check_raw_ent)

        # Import the raw datasets
        #########################
        dfile = eval("settings.check_raw" + fnum)
        if dfile.lower().endswith(('.xls', '.xlsx')):
            exec("settings.check_rawdata" + fnum + "= pd.read_excel(settings.check_raw" + fnum + ")")
        elif dfile.lower().endswith(('.csv')):
            exec(f"settings.check_rawdata{fnum} = pd.read_csv(settings.check_raw{fnum})")

        # Set ID widgets and other widgets that depend on the dataset
        #############################################################

        if dfile != '':
            selected_files.append(fnum)
            idvars = eval(f"settings.check_rawdata{fnum}.columns.tolist()")  # Get columns
            inc = fn * 2

            # Define widgets for selection of IDS variable
            exec(f"settings.id_ent{fnum}= Entry(checks_set_frame,  width=20, font=('Airial', 10))")
            idsel = ttk.Combobox(checks_set_frame, values=idvars, width=22)
            idsel.bind('<<ComboboxSelected>>', lambda event, entry=idsel, num=str(fnum), name='id_ent': combo_callback(entry.get(), num,name))
            exec(f"settings.checks_id{fnum} = idsel")
            exec(f"settings.checks_id{fnum}.set('Select ID variable')")
            exec(f"settings.checks_id{fnum}.grid(row={fn * 4}, column=3,ipady=3)")
            exec(f"settings.id_ent{fnum}.grid(row={fn * 4 +1}, column=3)")

            # Define widgets for selection of Variables to keep
            exec(f"settings.keep_ent{fnum}= Entry(checks_set_frame,  width=20, font=('Airial', 10))")
            exec(f"settings.keep_ent{fnum}.insert(0, 'ALL')")
            keepsel = ttk.Combobox(checks_set_frame, values=idvars, width=22)
            keepsel.bind('<<ComboboxSelected>>',
                       lambda event, entry=keepsel, num=str(fnum), name='keep_ent': combo_callback(entry.get(), num,name))  # callback function when combobox changes
            exec(f"settings.keepsel{fnum} = keepsel")
            exec(f"settings.keepsel{fnum}.set('Variables to keep')")
            exec(f"settings.keep_ent{fnum}.grid(row={fn * 4 + 1}, column=5)")
            exec(f"settings.keepsel{fnum}.grid(row={fn * 4}, column=5,ipady=3)")
            Label(checks_set_frame, text='',font=('Airial', 12), bg=checkssetbg).grid(row=fn * 4, column=4, padx=12)

            # Check box for checking which datasets to run
            exec(f"settings.run{fnum} = tk.IntVar()")
            ckb = tk.Checkbutton(checks_set_frame, text=f'Check Dataset {fnum}',bg=eval(f"datacol{fnum}")
                                 ,variable=eval(f"settings.run{fnum}"),command=lambda num=fnum: enable_checks(num))
            exec(f"settings.ckb{fnum}=ckb")
            exec(f"settings.ckb{fnum}.grid(row={inc + 26}, column = 1, sticky = 'NSEW') ")
            exec(f"Label(checks_set_frame, text=' ', bg=checkssetbg,font=('Airial', 1)).grid(row={inc + 27}, column=1)")

            # Widgets for checking which cecks to run
            exec(f"settings.dp{fnum} = tk.Checkbutton(checks_set_frame, text='',bg= checksbg1, variable=settings.dup{fnum},state=DISABLED)")
            exec(f"settings.ms{fnum} = tk.Checkbutton(checks_set_frame, text='',bg= checksbg2, variable=settings.miss{fnum},state=DISABLED)")
            exec(f"settings.ol{fnum} = tk.Checkbutton(checks_set_frame, text='',bg= checksbg3, variable=settings.outl{fnum},state=DISABLED)")
            exec(f"settings.ot{fnum} = tk.Checkbutton(checks_set_frame, text='',bg= checksbg4, variable=settings.other{fnum},state=DISABLED)")
            exec(f"settings.bo{fnum} = tk.Checkbutton(checks_set_frame, text='',bg= checksbg5, variable=settings.bound{fnum},state=DISABLED)")
            exec(f"settings.tb{fnum} = tk.Checkbutton(checks_set_frame, text='',bg= checksbg6, variable=settings.tabu{fnum},state=DISABLED)")

            exec(f"settings.dp{fnum}.grid(row={inc + 26}, column=3, sticky=W, pady=2)")
            exec(f"settings.ms{fnum}.grid(row={inc + 26}, column=3,  pady=2)")
            exec(f"settings.ol{fnum}.grid(row={inc + 26}, column=3, sticky=E, pady=2)")
            exec(f"settings.ot{fnum}.grid(row={inc + 26}, column=5, sticky=W, pady=2)")
            exec(f"settings.bo{fnum}.grid(row={inc + 26}, column=5,  pady=2)")
            exec(f"settings.tb{fnum}.grid(row={inc + 26}, column=5, sticky=E, pady=2)")

            # Place the update button with grid
            upd_cecks.grid(row=37, column=3, columnspan=3)
            rrun_cecks.grid(row=37, column=1)

            # Set header for checkboxes
            #Label(checks_set_frame, text=" ", bg=checkssetbg).grid(row=24, column=1)
            Label(checks_set_frame, text="Select Datasets to check", bg=checkssetbg,
                  font=('Airial', 12)).grid(row=25, column=1, rowspan=2, columnspan=2)
            Label(checks_set_frame, text="Select checks to run", bg=checkssetbg,
                  font=('Airial', 12)).grid(row=25, column=5, sticky=NSEW, padx=2)
            Label(checks_set_frame, text="", bg=checkssetbg,
                  font=('Airial', 2)).grid(row=25, column=4, sticky=NSEW, padx=2)

            # Set header for selection of checks
            Label(checks_set_frame, text="Dups", bg=checkssetbg, font=('Airial', 8)).grid(row=27, column=3, sticky=W)
            Label(checks_set_frame, text="Miss", bg=checkssetbg, font=('Airial', 8)).grid(row=27, column=3)
            Label(checks_set_frame, text="Outl", bg=checkssetbg, font=('Airial', 8)).grid(row=27, column=3, sticky=E)

            Label(checks_set_frame, text="Other", bg=checkssetbg, font=('Airial', 8)).grid(row=27, column=5, sticky=W)
            Label(checks_set_frame, text="Bound", bg=checkssetbg, font=('Airial', 8)).grid(row=27, column=5)
            Label(checks_set_frame, text="Tab", bg=checkssetbg, font=('Airial', 8)).grid(row=27, column=5, sticky=E)

        root.update()  # Update root


    # Define widgets for selection of rawdata
    ########################################
    for j in range(5):
        jn = str(j + 1)
        # Define the buttons and fields for the settings. ## Select data column
        exec("check_raw" + jn + "_ent = tk.StringVar()")
        exec("settings.check_raw" + jn + "_ent = check_raw" + jn + "_ent")
        exec("c_lab" + jn + "= Label(checks_set_frame, text=' " + jn + ": ', bg=checkssetbg, font=('Airial', 9))")
        exec("check_raw" + jn + "_ent = Entry(checks_set_frame, width=25, font=('Airial', 9), textvariable=check_raw" + jn + "_ent)")
        exec("check_raw" + jn + "_sel = Button(checks_set_frame,  text='Click to Select Dataset " + jn + "' "
                                    f",bg = datacol{jn}, fg = white,font=('Airial', 9,'bold'), width=24, command = lambda fname = 'checkraw" + jn + "': sel_file(fname))")
        exec("c_space" + jn + " =Label(checks_set_frame, text= '', bg=checkssetbg, font=('Airial', 1))")
    # Place the widgets for the first data.
    exec("check_raw1_sel.grid(row= 4 , column=1)")
    exec("check_raw1_ent.grid(row= 5  , column=1)")
    exec("c_lab1.grid(row= 4, rowspan=3, column=0, sticky=E)")
    exec("c_space1.grid(row=6, column=0, padx=1)")


    ########################
    # Check frames Placement
    # ######################

    # Check 1
    Label(checks_frame1, text="Check for Duplicates", bg=checksbg1,
          font=('Airial', 12, "bold", "underline")).grid(row=0, column=1, pady=2)
    dpon = Label(checks_frame1, text='Duplicates on', font=('Airial', 7), bg=checksbg1)
    dpsellb = Label(checks_frame1, text='Select ID var(s)', font=('Airial', 7), bg=checksbg1)

    # Check 2
    Label(checks_frame2, text="Check for Missing Values", bg=checksbg2,
          font=('Airial', 12, "bold", "underline")).grid(row=0, column=1,columnspan=5, pady=2, sticky=NSEW)
    # misson = Label(checks_frame2, text='Missing Check Variables', font=('Airial', 10), bg=checksbg2)
    misssellb = Label(checks_frame2, text='Select Variables(s) to check for missing', font=('Airial', 12, 'bold'), bg=checksbg2)

    # Check 3
    Label(checks_frame3, text="Check for Outliers", bg=checksbg3,
          font=('Airial', 12, "bold", "underline")).grid(row=0, column=1,columnspan=5, pady=2, sticky=NSEW)
    # outlon = Label(checks_frame3, text='outling Check Variables', font=('Airial', 10), bg=checksbg3)
    outlsellb = Label(checks_frame3, text='Select Variables(s) to check outliers on', font=('Airial', 12, 'bold'), bg=checksbg3)

    # Check 4
    Label(checks_frame4, text="Other Specify Check", bg=checksbg4,
          font=('Airial', 12, "bold", "underline")).grid(row=0, column=1,columnspan=5, pady=1, sticky=NSEW)
    plab = Label(checks_frame4, text="Parent",bg=checksbg4,font=('Airial', 11, "bold"))
    clab = Label(checks_frame4, text="Child",bg=checksbg4,font=('Airial', 11, "bold"))

    # Check 5
    Label(checks_frame5, text="Boundary/Constraint Check", bg=checksbg5,
          font=('Airial', 12, "bold", "underline")).grid(row=0, column=1,columnspan=5, pady=1, sticky=NSEW)
    bplab = Label(checks_frame5, text="Viriable",bg=checksbg5,font=('Airial', 11, "bold"))
    bllab = Label(checks_frame5, text="Lower",bg=checksbg5,font=('Airial', 11, "bold"))
    bulab = Label(checks_frame5, text="Upper",bg=checksbg5,font=('Airial', 11, "bold"))

    # Check 6
    Label(checks_frame6, text="Tabulations and Others", bg=checksbg6, \
          font=('Airial', 17, "bold", "underline")).grid(row=1, column=0, columnspan=2, pady=2)


    # Define Color Codes for Data headlines
    # Update widgets in the six checks
    # ################################
    def update_checks():

        # Get number of buttons checks for each check type and for the datasets
        n_data_tocheck = settings.run1.get() + settings.run2.get() + settings.run3.get() + settings.run4.get() + settings.run5.get()
        num_dups_sel = settings.dup1.get() + settings.dup2.get() + settings.dup3.get() + settings.dup4.get() + settings.dup5.get()
        num_miss_sel = settings.miss1.get() + settings.miss2.get() + settings.miss3.get() + settings.miss4.get() + settings.miss5.get()
        num_outl_sel = settings.outl1.get() + settings.outl2.get() + settings.outl3.get() + settings.outl4.get() + settings.outl5.get()
        num_other_sel = settings.other1.get() + settings.other2.get() + settings.other3.get() + settings.other4.get() + settings.other5.get()
        num_bound_sel = settings.bound1.get() + settings.bound2.get() + settings.bound3.get() + settings.bound4.get() + settings.bound5.get()
        num_tabu_sel = settings.tabu1.get() + settings.tabu2.get() + settings.tabu3.get() + settings.tabu4.get() + settings.tabu5.get()

        # ##################################
        # Place Header Widgets for all checks
        # ###################################
        dpon.grid(row=1, column=2, sticky=NSEW)
        dpsellb.grid(row=1, column=1, sticky=NSEW)
        #misson.grid(row=1, column=2, sticky=NSEW)
        misssellb.grid(row=1, column=1, sticky=NSEW, columnspan=5)
        #outlon.grid(row=1, column=2, sticky=NSEW)
        outlsellb.grid(row=1, column=1, sticky=NSEW, columnspan=5)
        plab.grid(row=3, column=0, sticky=E)
        clab.grid(row=4, column=0, sticky=E)
        bplab.grid(row=3, column=0, sticky=E)
        bllab.grid(row=4, column=0, sticky=E)
        bulab.grid(row=5, column=0, sticky=E)

        # ##############################################
        # Function to place widgets of selected dups
        # ###############################################
        for i in list(set(selected_files)):
            i = int(i)

            datavars = eval(f"settings.check_rawdata{i}.columns.tolist()")  # Get columns

            # ######################
            # Check 2
            # Place Missing Widgets
            # ######################
            checked_dp = eval(f"settings.dup{i}.get()")

            # Remove already existing widgets that aren't neccesary
            try:
                exec(f"settings.dupn{i}.grid_forget()")
                exec(f"settings.dup_id_ent{i}.grid_forget()")
                exec(f"settings.dpsel{i}.grid_forget()")
            except:
                pass

            # place widgets
            if (checked_dp == 1):
                exec(f"settings.dupn{i} = Label(checks_frame1, text='Dataset {i}',fg='#FFFFFF',bg=datacol{i})")
                exec(f"settings.dup_id_ent{i}= Entry(checks_frame1,  width=25, font=('Airial', 10))")
                exec(f"settings.dup_id_ent{i}.insert(0, settings.checks_id{i}.get())")
                dpsel = ttk.Combobox(checks_frame1, values=datavars)
                dpsel.bind('<<ComboboxSelected>>', lambda event, entry=dpsel, num=str(i), name='dup_id_ent': combo_callback(entry.get(),num, name))  # callback function when combobox changes
                dpsel.set(eval(f"settings.checks_id{i}.get()"))
                exec(f"settings.dpsel{i} = dpsel")

                # Place widgets for duplicates section
                dpsel.grid(row=i + 2, column=1, ipady=5, padx=2)
                exec(f"settings.dup_id_ent{i}.grid(row={i + 2}, column=2, pady=2,sticky=NSEW)")
                exec(f"settings.dupn{i}.grid(row={i + 2}, column=0,sticky=W)")
            # remove widgets for the duplicates section
            if(checked_dp == 0):
                try:
                    exec(f"settings.dupn{i}.grid_forget()")
                    exec(f"settings.dup_id_ent{i}.grid_forget()")
                    exec(f"settings.dpsel{i}.grid_forget()")
                except:
                    pass


            # ######################
            # Check 2
            # Place Missing Widgets
            # ######################
            checked_miss = eval(f"settings.miss{i}.get()")

            # Remove already existing widgets that aren't neccesary
            try:
                exec(f"settings.missn{i}.grid_forget()")
                exec(f"settings.miss_id_ent{i}.grid_forget()")
                exec(f"settings.misssel{i}.grid_forget()")
            except:
                pass

            # place widgets
            if (checked_miss == 1):
                exec(f"settings.missn{i} = Label(checks_frame2, text='Dataset {i}',fg='#FFFFFF',bg=datacol{i},font=('Airial', 11, 'bold'))")
                exec(f"settings.miss_id_ent{i}= Text(checks_frame2,  height = 12, width = 20, font=('Airial', 10))")
                exec(f"settings.miss_id_ent{i}.insert(END, settings.checks_id{i}.get() + ',\\n' )")
                misssel = ttk.Combobox(checks_frame2, values=datavars, width=21)
                misssel.bind('<<ComboboxSelected>>', lambda event, entry=misssel, num=str(i), name='miss_id_ent': combo_callback(entry.get(),num, name))  # callback function when combobox changes
                misssel.set(eval(f"settings.checks_id{i}.get()"))
                exec(f"settings.misssel{i} = misssel")

                # Place widgets for duplicates section
                misssel.grid(row=3, column=i + 2, ipady=5, padx =2)
                exec(f"settings.miss_id_ent{i}.grid(row=4, column={i + 2}, pady =2,padx =2)")
                exec(f"settings.missn{i}.grid(row=2, column=i + 2,padx =3,sticky=NSEW)")
            # remove widgets for the duplicates section
            if(checked_miss == 0):
                try:
                    exec(f"settings.missn{i}.grid_forget()")
                    exec(f"settings.miss_id_ent{i}.grid_forget()")
                    exec(f"settings.misssel{i}.grid_forget()")
                except:
                    pass

            # ######################
            # Check 3
            # Place Outlier Widgets
            # ######################
            checked_outl = eval(f"settings.outl{i}.get()")

            # Remove already existing widgets that aren't neccesary
            try:
                exec(f"settings.outln{i}.grid_forget()")
                exec(f"settings.outl_id_ent{i}.grid_forget()")
                exec(f"settings.outlsel{i}.grid_forget()")
            except:
                pass

            # place widgets
            if (checked_outl == 1):
                exec(f"settings.outln{i} = Label(checks_frame3, text='Dataset {i}',fg='#FFFFFF',bg=datacol{i},font=('Airial', 11, 'bold'))")
                exec(f"settings.outl_id_ent{i}= Text(checks_frame3,  height = 12, width = 20, font=('Airial', 10))")
                exec(f"settings.outl_id_ent{i}.insert(END, settings.checks_id{i}.get() + ',\\n' )")
                outlsel = ttk.Combobox(checks_frame3, values=datavars, width=21)
                outlsel.bind('<<ComboboxSelected>>', lambda event, entry=outlsel, num=str(i), name='outl_id_ent': combo_callback(entry.get(),num, name))  # callback function when combobox changes
                outlsel.set(eval(f"settings.checks_id{i}.get()"))
                exec(f"settings.outlsel{i} = outlsel")

                # Place widgets for duplicates section
                outlsel.grid(row=3, column=i + 2, ipady=5, padx =2)
                exec(f"settings.outl_id_ent{i}.grid(row=4, column={i + 2}, pady =2,padx =2)")
                exec(f"settings.outln{i}.grid(row=2, column=i + 2,ipadx =3,padx =3,sticky=NSEW)")
            # remove widgets for the duplicates section
            if(checked_outl == 0):
                try:
                    exec(f"settings.outln{i}.grid_forget()")
                    exec(f"settings.outl_id_ent{i}.grid_forget()")
                    exec(f"settings.outlsel{i}.grid_forget()")
                except:
                    pass


            # ######################
            # Check 4
            # Place OtherSpecify Widgets
            # ######################
            checked_other = eval(f"settings.other{i}.get()")

            # Remove already existing widgets that aren't neccesary
            try:
                exec(f"settings.othern{i}.grid_forget()")
                exec(f"settings.other_id_ent{i}.grid_forget()")
                exec(f"settings.othersel_p{i}.grid_forget()")
                exec(f"settings.othersel_c{i}.grid_forget()")
                exec(f"settings.other_butt{i}.grid_forget()")
            except:
                pass

            # place widgets
            if (checked_other == 1):
                exec(f"settings.othern{i} = Label(checks_frame4, text='Dataset {i}',fg='#FFFFFF',bg=datacol{i},font=('Airial', 11, 'bold'))")
                exec(f"settings.other_id_ent{i}= Text(checks_frame4,  height = 12, width = 20, font=('Airial', 10))")
                othersel_p = ttk.Combobox(checks_frame4, values=datavars, width=21)
                othersel_c = ttk.Combobox(checks_frame4, values=datavars, width=21)
                other_butt = Button(checks_frame4, text="Add 👇👇",width=10, command=lambda entry1= othersel_p, entry2= othersel_c,
                                num=str(i), name='other_id_ent': combo_callback(entry1.get() + "|" + entry2.get(),num, name))
                #othersel.bind('<<ComboboxSelected>>', lambda event, entry=othersel, num=str(i), name='other_id_ent': combo_callback(entry.get(),num, name))  # callback function when combobox changes
                exec(f"settings.othersel_p{i} = othersel_p")
                exec(f"settings.othersel_c{i} = othersel_c")
                exec(f"settings.other_butt{i} = other_butt")

                # Place widgets for duplicates section
                exec(f"settings.othersel_p{i}.grid(row=3, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.othersel_c{i}.grid(row=4, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.other_butt{i}.grid(row=5, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.other_id_ent{i}.grid(row=6, column={i + 2}, pady =2,padx =2)")
                exec(f"settings.othern{i}.grid(row=2, column=i + 2,ipadx =3,padx =3,sticky=NSEW)")
            # remove widgets for the duplicates section
            if(checked_other == 0):
                try:
                    exec(f"settings.othern{i}.grid_forget()")
                    exec(f"settings.other_id_ent{i}.grid_forget()")
                    exec(f"settings.othersel_p{i}.grid_forget()")
                    exec(f"settings.othersel_c{i}.grid_forget()")
                    exec(f"settings.other_butt{i}.grid_forget()")
                except:
                    pass


            # ######################
            # Check 5
            # Place Bound/Constraint Widgets
            # ######################
            checked_bound = eval(f"settings.bound{i}.get()")

            # Remove already existing widgets that aren't neccesary
            try:
                exec(f"settings.boundn{i}.grid_forget()")
                exec(f"settings.bound_id_ent{i}.grid_forget()")
                exec(f"settings.boundsel_p{i}.grid_forget()")
                exec(f"settings.boundsel_c{i}.grid_forget()")
                exec(f"settings.boundsel_u{i}.grid_forget()")
                exec(f"settings.bound_butt{i}.grid_forget()")
            except:
                pass

            # place widgets
            if (checked_bound == 1):
                exec(f"settings.boundn{i} = Label(checks_frame5, text='Dataset {i}',fg='#FFFFFF',bg=datacol{i},font=('Airial', 11, 'bold'))")
                exec(f"settings.bound_id_ent{i}= Text(checks_frame5,  height = 12, width = 20, font=('Airial', 10))")
                boundsel_p = ttk.Combobox(checks_frame5, values=datavars, width=21)
                boundsel_c = ttk.Entry(checks_frame5, width=23)
                boundsel_u = ttk.Entry(checks_frame5, width=23)
                bound_butt = Button(checks_frame5, text="Add 👇👇",width=10, command=lambda entry1= boundsel_p,
                                entry2= boundsel_c,entry3= boundsel_u,num=str(i), name='bound_id_ent': combo_callback(entry1.get()
                                + "|" + entry2.get()+ "|" + entry3.get(),num, name))
                #boundsel.bind('<<ComboboxSelected>>', lambda event, entry=boundsel, num=str(i), name='bound_id_ent': combo_callback(entry.get(),num, name))  # callback function when combobox changes
                exec(f"settings.boundsel_p{i} = boundsel_p")
                exec(f"settings.boundsel_c{i} = boundsel_c")
                exec(f"settings.boundsel_u{i} = boundsel_u")
                exec(f"settings.bound_butt{i} = bound_butt")

                # Place widgets for duplicates section
                exec(f"settings.boundsel_c{i}.grid(row=4, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.boundsel_p{i}.grid(row=3, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.boundsel_u{i}.grid(row=5, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.bound_butt{i}.grid(row=6, column=i + 2, ipady=5, padx =2)")
                exec(f"settings.bound_id_ent{i}.grid(row=7, column={i + 2}, pady =2,padx =2)")
                exec(f"settings.boundn{i}.grid(row=2, column=i + 2,ipadx =3,padx =3,sticky=NSEW)")
            # remove widgets for the duplicates section
            if(checked_bound == 0):
                try:
                    exec(f"settings.boundn{i}.grid_forget()")
                    exec(f"settings.bound_id_ent{i}.grid_forget()")
                    exec(f"settings.boundsel_p{i}.grid_forget()")
                    exec(f"settings.boundsel_c{i}.grid_forget()")
                    exec(f"settings.boundsel_u{i}.grid_forget()")
                    exec(f"settings.bound_butt{i}.grid_forget()")
                except:
                    pass



        # Remove the label that says check dp on
        if num_dups_sel == 0:
            dpon.grid_forget()
            dpsellb.grid_forget()
        if num_miss_sel == 0:
            # misson.grid_forget()
            misssellb.grid_forget()
        if num_outl_sel == 0:
            # outlon.grid_forget()
            outlsellb.grid_forget()
        if num_other_sel == 0:
            plab.grid_forget()
            clab.grid_forget()
        if num_bound_sel == 0:
            bplab.grid_forget()
            bllab.grid_forget()
            bulab.grid_forget()

        # ##################################
        # Place Widgets on miss frame
        # ###################################





        root.update()



    upd_cecks = Button(checks_set_frame, text='Update', font=('Tahoma', 12), height=1, bg='skyblue1', width=22,
                       command=update_checks)

    # ###################
    # CALL CHECKS SCRIPTS
    #####################

    # DUPLICATES
    # ##########

    settings.checks_fame = checks_set_frame
    def run_all_checks():

        tday = date.today()
        today = tday.strftime("%b-%d-%Y")
        main_folder = settings.parent_folder

        selectedvars = list(set(selected_files))
        # Remove datasets that have been discontinued
        for k in range(1,6):
            nfs = settings.num_data_files
            if str(k) in selectedvars and k > nfs and nfs >=1:
                selectedvars.remove(str(k))
            outfolder = main_folder + f"/4_output/Data {k}/{today}"
            if not os.path.exists(outfolder) and str(k) in selectedvars:
                os.makedirs(outfolder)
            #print(eval(f"settings.miss_id_ent{k}.get(1.0, END)"))

        # Call the checks
        checks_duplicate.run_check(selectedvars, main_folder, today)     # Call duplicates check
        checks_missing.run_check(selectedvars, main_folder, today)     # Call Miss check
        checks_outliers.run_check(selectedvars, main_folder, today)
        checks_boundary.run_check(selectedvars, main_folder, today)
        checks_other_specify.run_check(selectedvars, main_folder, today)

        # Completion note
        settings.erdlabel = tk.Label(checks_set_frame,
                            text=f"All Checks Completed",
                            background="green", foreground="white", font=('Airial', 20, "bold"))
        settings.erdlabel.grid(row=40, column=0, columnspan=5)
        settings.erdlabel.after(10000, settings.erdlabel.destroy)

    # Buttons to call checks function
    rrun_cecks = Button(checks_set_frame, text='Run Checks', font=('Tahoma', 12), height=1, bg='skyblue2', width=22,
                       command=run_all_checks)




    # ###############
    # Session Control
    # ###############

    # Callback function to activate session control
    def restore_callback(option):

        if settings.folder_name != '':
            res = os.listdir(settings.folder_name)
            for j in res:
                if j.endswith('.json'):
                    p_ss_name = j.split('.json')[0]
                    ss_name_list.append(p_ss_name)
        ssc_name_ent.config(values=ss_name_list)
        ssc_loc_ent.insert(0, settings.folder_name)             # Insert parent folder initially

        settings.session_type = option
        if option == 'Restore Session':

            # update Session widget
            ssc_loc_butt.grid(row=44, column=1)
            ssc_loc_ent.grid(row=45, column=1)
            ssc_name_ent.grid(row=44, column=3, columnspan=3)
            ssc_version_ent.grid(row=45, column=3, columnspan=3)
            ssc_name.grid(row=44, column=3, sticky=W)
            ssc_vers.grid(row=45, column=3, sticky=W)
            ssc_res_butt.grid(row=44, column=5, sticky=E, rowspan=2)
            ssc_name_ent1.grid_remove()
            settings.session_folder = settings.folder_name

        elif option=="Save_session":
            ssc_name_ent.grid_remove()
            ssc_name_ent1.grid(row=44, column=3, columnspan=3)
            ssc_loc_butt.grid(row=44, column=1)
            ssc_loc_ent.grid(row=45, column=1)
            ssc_version_ent.grid(row=45, column=3, columnspan=3)
            ssc_name.grid(row=44, column=3, sticky=W)
            ssc_vers.grid(row=45, column=3, sticky=W)
            ssc_res_butt.grid(row=44, column=5, sticky=E, rowspan=2)
            settings.session_folder = settings.folder_name


        else:
            ssc_loc_butt.grid_remove()
            ssc_loc_ent.grid_remove()
            ssc_name_ent.grid_remove()
            ssc_version_ent.grid_remove()
            ssc_name.grid_remove()
            ssc_vers.grid_remove()


    # Callback function to select the folder for session control
    def restor_callfold():

        dialogs.get_folder()
        ssc_loc_ent.delete(0, END)
        settings.session_folder = settings.folder_name

        # update list
        ss_name_list = []
        res = os.listdir(settings.folder_name)
        for j in res:
            if j.endswith('.json'):
                p_ss_name = j.split('.json')[0]
                ss_name_list.append(p_ss_name)
        ssc_name_ent.config(values=ss_name_list)
        ssc_loc_ent.insert(0, settings.folder_name)             # Insert parent folder initially


    # Callback Function for session control
    # Executes the various session controls
    def restor_run_call():
        #settings.session_type = '';
        settings.session_folder = settings.folder_name;
        settings.session_file = ssc_name_ent.get() or ssc_name_ent1.get()

        settings.num_raw_files = num_files_val.get()
        settings.num_data_files = num_data_val.get()

        settings.session_version = ssc_version_ent.get()
        session_control.run_session_control(settings.session_type,
                    settings.session_folder, settings.session_file, settings.session_version)

        # Populate fields for Restoration
        if ssc_opt_butt.get() == "Restore Session":
            num_data_val.set(int(settings.num_data_files))
            #update_check_number(settings.num_data_files)


            # update ID and keep widgets at the check settings
            for num in range(1, int(settings.num_data_files) + 1):
                sel_file(f"Restore{num}")

            # Update checks Setting widgets
            update_check_number(int(settings.num_data_files))

            # Populate Entry and combo fields in checks settings
            for i in range(1, int(settings.num_data_files) + 1):
                exec(f"check_raw{i}_ent.insert(0, settings.check_raw{i}_ent)")
                exec(f"settings.keep_ent{i}.delete(0, END)")
                exec(f"settings.id_ent{i}.delete(0, END)")
                exec(f"settings.keep_ent{i}.insert(0, settings.r_keep_ent{i})")
                exec(f"settings.id_ent{i}.insert(0, settings.r_id_ent{i})")

                # Combo Check boxes to activate the checks
                exec(f"settings.run{i}.set(settings.r_run{i})")
                exec(f"settings.dup{i}.set(settings.r_dup{i})")
                exec(f"settings.miss{i}.set(settings.r_miss{i})")
                exec(f"settings.outl{i}.set(settings.r_outl{i})")
                exec(f"settings.bound{i}.set(settings.r_bound{i})")
                exec(f"settings.other{i}.set(settings.r_other{i})")
                exec(f"settings.tabu{i}.set(settings.r_tabu{i})")

                # Control the state of the various check buttons
                # Call the enable_checks() function
                enable_checks(f"{i}")

            # Refresh and populate the Checks windows
            update_checks()
            for i in range(1, int(settings.num_data_files) + 1):
                # Populate widgets for only datasets that are selected
                try:
                    exec(f"settings.dup_id_ent{i}.delete(0, END)")
                    exec(f"settings.dup_id_ent{i}.insert(0, settings.r_dup_id_ent{i})")
                    exec(f"settings.miss_id_ent{i}.delete(1.0, END)")
                    exec(f"settings.miss_id_ent{i}.insert(1.0, settings.r_miss_id_ent{i})")
                    exec(f"settings.outl_id_ent{i}.delete(1.0, END)")
                    exec(f"settings.outl_id_ent{i}.insert(1.0, settings.r_outl_id_ent{i})")
                    exec(f"settings.other_id_ent{i}.delete(1.0, END)")
                    exec(f"settings.other_id_ent{i}.insert(1.0, settings.r_other_id_ent{i})")
                    exec(f"settings.bound_id_ent{i}.delete(1.0, END)")
                    exec(f"settings.bound_id_ent{i}.insert(1.0, settings.r_bound_id_ent{i})")
                except:
                    pass
                if eval(f"settings.check_raw{i}.lower().endswith(('.xls', '.xlsx'))"):
                    exec("settings.check_rawdata" + i + "= pd.read_excel(settings.check_raw" + i + ")")
                    #msg.showinfo("Imported-XLS")
                elif eval(f"settings.check_raw{i}.lower().endswith(('.csv'))"):
                    exec(f"settings.check_rawdata{i} = pd.read_csv(settings.check_raw{i})")
                    #msg.showinfo("Imported-CSV")

        # Populate
        root.update()
        msg.showinfo("Success", "This previous session has been restored.")



    ssc_lab = Label(checks_set_frame,text=f"Session Control →", bg =checkssetbg , font=('Airial', 14, "bold"))
    ssc_lab.grid(row = 42, column=1, columnspan=2, sticky=E)

    ssc_opts = ("","Restore Session", "Save_session", "Update_session",)
    ssc_opt_butt = ttk.Combobox(checks_set_frame, values=ssc_opts, width=21)
    ssc_opt_butt.bind('<<ComboboxSelected>>', lambda event, option=ssc_opt_butt:restore_callback(option.get()))  # callback function when combobox changes
    ssc_opt_butt.set(" Session Option")
    ssc_opt_butt.grid(row=42, column=3)

    # Set widgets for project restoration
    ssc_loc_butt = Button(checks_set_frame, text='Session_location(opt)', font=('Tahoma', 12), height=1, width=20,
                       command=restor_callfold)
    ssc_loc_ent = ttk.Entry(checks_set_frame, width=30)
    ssc_name= Label(checks_set_frame, text="Name",font=('Airial', 11, 'bold'), bg=checkssetbg)
    ssc_vers=Label(checks_set_frame, text="version",font=('Airial', 10, 'bold'), bg=checkssetbg)
    ssc_version_ent = ttk.Entry(checks_set_frame, width=18)


    # Get previous sessions in current folder
    # #######################################

    ss_name_list = []
    ssc_name_ent = ttk.Combobox(checks_set_frame, values=ss_name_list, width=18)
    ssc_name_ent1 = ttk.Entry(checks_set_frame, width=18)

    ssc_res_butt = Button(checks_set_frame, text='RUN',bg='skyblue1', font=('Tahoma', 12), height=3, width=5,
                       command=restor_run_call)















    # Root parameters
    main_frame = Frame(root)
    main_frame.pack()

    root.title("PRC DATA CHECK SOLUTION", )
    # root.maxsize(800,  500)  # width x height
    # root.resizable(False, False)
    root.mainloop()


