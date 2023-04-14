# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Exports other-specify responses
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


# Define check function
def run_check(num, main_folder, today):

    # Set labels for progress:
    try:
        settings.erdlabel.grid_remove()
    except:
        pass
    settings.erdlabel = tk.Label(settings.checks_fame,
                        text=f"Exporting Other-Specified Values",
                        background="blue", foreground="white", font=('Airial', 20, "bold"))
    settings.erdlabel.grid(row=40, column=0, columnspan=5)

    # Loop throuth the selected datasets
    for k in range(len(num)):
        ind = num[k]

        # Call global vars
        # ################
        run_check = eval(f"settings.run{ind}.get()")
        run_other = eval(f"settings.other{ind}.get()")
        outfolder = main_folder + f"/4_output/Data {ind}/{today}"

        if run_check ==1 and run_other ==1:
            settings.erdlabel.config(text=f"Exporting Other-Specified Values for Data{ind}")

            data_id = eval(f"settings.id_ent{ind}.get()")
            other_vars = eval(f"settings.other_id_ent{ind}.get('1.0', 'end-1c').replace('\\n','')")
            keep_vars = eval(f"settings.keep_ent{ind}.get().split(',')")
            other_vars_list =  eval("other_vars.split(',')")
            df = eval(f"settings.check_rawdata{ind}")
            for i in ['parent_var_name', 'child_var_name', 'Child_specified_value']:
                keep_vars.append(i)
                df[i] = ''
            keep_vars.insert(0, data_id)  # Put Data ID as part of keep variables
            final_df = []  # Predefine the final outcome dataset
            df_cols = df.columns.tolist()
            other_vars_list.remove("")
            for j in other_vars_list:

                # Get variable name, lower-bound and upper bound
                parent_variable_ = j.split('|')[0]
                child_variable_ = j.split("|")[1]
                # Ignore empty items
                if parent_variable_ in df_cols and child_variable_ in df_cols and child_variable_ != '':

                    df['parent_var_name'] = parent_variable_
                    df['child_var_name'] = child_variable_
                    df['Child_specified_value'] = df[child_variable_]

                    df_new = df[df['Child_specified_value'].notna()]
                    df_new = df_new[keep_vars]

                    final_df.append(df_new)
                elif parent_variable_ not in df_cols:
                    msg.showerror("Other Specify Error",
                                  f"No child value specified for {parent_variable_} in Data{ind}")
                elif parent_variable_ not in df_cols:
                    msg.showerror("Bound check Error", f"No Parent value specified for {child_variable_} in Data{ind}")

            final_df = pd.concat(final_df).reset_index()
            final_df = final_df[keep_vars]

            # Export to Excel
            mode = ''
            if os.path.exists(f'{outfolder}/Check_Output.xlsx'):
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx', mode = 'a', if_sheet_exists='replace') as writer:
                    final_df.to_excel(writer, sheet_name='Other-Specify',index=False)
            else:
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx') as writer:
                    final_df.to_excel(writer, sheet_name='Other-Specify',index=False)

            settings.erdlabel.grid_remove()
