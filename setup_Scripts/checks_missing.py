# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Checks missing values
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
# -------------------------------------
import pandas as pd
import numpy as np
import openpyxl
from tkinter import messagebox as msg
import numpy as np
import tkinter as tk
import os


import settings




# Duplicates check
def run_check(num, main_folder, today):


    # Set labels for progress:
    try:
        settings.erdlabel.grid_remove()
    except:
        pass
    settings.erdlabel = tk.Label(settings.checks_fame,
                        text=f"Running Missing Checks check",
                        background="blue", foreground="white", font=('Airial', 20, "bold"))
    settings.erdlabel.grid(row=40, column=0, columnspan=5)


    # Loop throuth the selected datasets
    for k in range(len(num)):
        ind = num[k]

        # Call global vars
        # ################
        run_check = eval(f"settings.run{ind}.get()")
        run_miss = eval(f"settings.miss{ind}.get()")
        outfolder = main_folder + f"/4_output/Data {ind}/{today}"

        if run_check ==1 and run_miss ==1:
            settings.erdlabel.config(text=f"Missing Check for for Data{ind}")

            data_id = eval(f"settings.id_ent{ind}.get()")
            miss_vars = eval(f"settings.miss_id_ent{ind}.get('1.0', 'end-1c').replace('\\n','')")
            #miss_vars =  miss_vars
            keep_vars = eval(f"settings.keep_ent{ind}.get().split(',')")

            miss_vars_list =  eval("miss_vars.split(',')")
            df = eval(f"settings.check_rawdata{ind}")
            print(miss_vars_list)

            # Loop through missing variables and check for missing
            df['miss_var_name'] = ''                        # Variable to keep name of missing column
            keep_vars.insert(0, data_id)                    # Put Data ID as part of keep variables
            keep_vars.append('miss_var_name')               # Add variable that keeps missing column names to keepvars
            final_df = []                                   # Predefine the final outcome dataset

            df_cols =  df.columns.tolist()
            for j in miss_vars_list:


                # Ignore empty items
                if j in df_cols:
                    df['miss_var_name'] = np.where(df[j].isnull(), j,
                                                   '')  # store the name of variable for all that have missing
                    fdf = df[df["miss_var_name"] != ''][keep_vars]
                    final_df.append(fdf)
                elif j != '':
                    msg.showerror("Invalid Variable",f" no variable names {j} in data {ind} ")

                    settings.erdlabel.grid_remove()

            final_df = pd.concat(final_df).reset_index()
            final_df = final_df[keep_vars]

            # Export  Output to Excel
            mode = ''
            if os.path.exists(f'{outfolder}/Check_Output.xlsx'):
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx', mode = 'a', if_sheet_exists='replace') as writer:
                    final_df.to_excel(writer, sheet_name='Missing',index=False)
            else:
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx') as writer:
                    final_df.to_excel(writer, sheet_name='Missing',index=False)
            settings.erdlabel.grid_remove()


