# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Checks Outliers
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
                        text=f"Running Outlier Checks check",
                        background="blue", foreground="white", font=('Airial', 20, "bold"))
    settings.erdlabel.grid(row=40, column=0, columnspan=5)

    # Loop throuth the selected datasets
    for k in range(len(num)):
        ind = num[k]

        # Call global vars
        # ################
        run_check = eval(f"settings.run{ind}.get()")
        run_outl = eval(f"settings.outl{ind}.get()")
        outfolder = main_folder + f"/4_output/Data {ind}/{today}"

        if run_check ==1 and run_outl ==1:
            settings.erdlabel.config(text=f"Outlier Check for for Data{ind}")

            data_id = eval(f"settings.id_ent{ind}.get()")
            outl_vars = eval(f"settings.outl_id_ent{ind}.get('1.0', 'end-1c').replace('\\n','')")
            keep_vars = eval(f"settings.keep_ent{ind}.get().split(',')")
            outl_vars_list =  eval("outl_vars.split(',')")
            df = eval(f"settings.check_rawdata{ind}")

            # Generate all neccesary output variables
            for i in ['outlier_var_name', 'actual_value', 'outlier_message']:
                keep_vars.append(i)
                df[i] = ''
            keep_vars.insert(0, data_id)  # Put Data ID as part of keep variables
            final_df = []  # Predefine the final outcome dataset
            df_cols = df.columns.tolist()

            # Loop through selected variable for outlier and check outlier
            for j in outl_vars_list:
                # Ignore empty items
                if j in df_cols:
                    try:
                        # print(j)
                        df['zscore'] = (df[j] - df[j].mean()) / df[j].std()
                        df['actual_value'] = df[j]
                        df['outlier_var_name'] = j
                        # Keep only outliers and pass outlier
                        df_new = df[(df.zscore < -3) | (df.zscore > 3)]
                        df_new['outlier_message'] = np.where(df_new.zscore < -3, "Potential Outlier: Z-score less than -3 ",
                                                         "Potential Outlier: Z-score more than 3 ")
                        print(keep_vars)
                        df_new = df_new[keep_vars]
                        print("New")
                        print("Never")
                        final_df.append(df_new)
                        print("New")
                        print(df_new)


                    except:
                        #msg.showerror("Invalid Variable", f"Cannot run outlier on {j} in data {k+1}.Program will skip")
                        pass
                elif j != '':
                    msg.showerror("Invalid Variable",f" No variable names {j} in data {k+1} ")

                    settings.erdlabel.grid_remove()

            final_df = pd.concat(final_df).reset_index()
            final_df = final_df[keep_vars]

            # Export  Output to Excel
            if os.path.exists(f'{outfolder}/Check_Output.xlsx'):
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx', mode = 'a', if_sheet_exists='replace') as writer:
                    final_df.to_excel(writer, sheet_name='Outliers',index=False)
            else:
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx') as writer:
                    final_df.to_excel(writer, sheet_name='Outliers',index=False)
            settings.erdlabel.grid_remove()


