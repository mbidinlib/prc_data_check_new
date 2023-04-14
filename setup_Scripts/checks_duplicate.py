# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Runs Duplicates check on datasets
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
# -------------------------------------
import pandas as pd
from tkinter import messagebox as msg
import tkinter as tk
from pathlib import Path

import settings


# Duplicates check
def run_check(num, main_folder, today):


    # Set labels for progress:
    try:
        settings.erdlabel.grid_remove()
    except:
        pass
    settings.erdlabel = tk.Label(settings.checks_fame,
                        text=f" Running Duplicates check",
                        background="blue", foreground="white", font=('Airial', 20, "bold"))
    settings.erdlabel.grid(row=40, column=0, columnspan=5)

    # Loop throuth the selected datasets
    for k in range(len(num)):
        ind = num[k]

        # Call global vars
        # ################
        run_check = eval(f"settings.run{ind}.get()")
        run_dup = eval(f"settings.dup{ind}.get()")
        outfolder = main_folder + f"/4_output/Data {ind}/{today}"

        if run_check ==1 and run_dup==1:
            dup_id = eval(f"settings.dup_id_ent{ind}.get()")
            keep_vars = eval(f"settings.keep_ent{ind}.get()")
            data_id = eval(f"settings.id_ent{ind}.get()")
            keep_vars =  data_id + "," + keep_vars

            dup_id_list =  eval("dup_id.split(',')")
            dataset = eval(f"settings.check_rawdata{ind}")

            # Attempt duplicate check
            try:
                #settings.erdlabel.config(text=f"Duplicates Check for for Data{ind}")

                if keep_vars == "ALL" or keep_vars =="":
                    dups = dataset[dataset.duplicated(eval("dup_id.split(',')"),
                                                      keep=False)].reset_index(drop=True)
                else:
                    dups = dataset[dataset.duplicated(eval("dup_id.split(',')"),
                                                      keep=False)][eval("keep_vars.split(',')")].reset_index(drop=True)
                final_df = dups
                # Export
                # Create a Pandas Excel writer using XlsxWriter as the engine.
                mode = ''
                if Path(f'{outfolder}/Check_Output.xlsx').is_file():
                    with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx', mode='a',
                                        if_sheet_exists='replace') as writer:
                        final_df.to_excel(writer, sheet_name='Duplicates', index=False)
                else:
                    with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx') as writer:
                        final_df.to_excel(writer, sheet_name='Duplicates', index=False)

            except KeyError:
                msg.showerror("Dups Check Error", f"One of your IDs or keep vriables are not in the data data {ind}")
                settings.erdlabel.destroy()
            except PermissionError:
                msg.showerror("File Opened", "The output file is opened. Please close and run again")
                settings.erdlabel.destroy()

        # Run duplicates check


