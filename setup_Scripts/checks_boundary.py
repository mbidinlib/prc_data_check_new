# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Runs Boundary/Constraint
#          check on datasets
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
# -------------------------------------
import pandas as pd
import numpy as np
import openpyxl
from tkinter import messagebox as msg
import numpy as np
import tkinter as tk
from scipy import stats
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pathlib import Path


import settings


# Define check function
def run_check(num, main_folder, today):

    # Set labels for progress:
    try:
        settings.erdlabel.grid_remove()
    except:
        pass
    settings.erdlabel = tk.Label(settings.checks_fame,
                        text=f"Running Boundary/Constraint Checks check",
                        background="blue", foreground="white", font=('Airial', 20, "bold"))
    settings.erdlabel.grid(row=40, column=0, columnspan=5)

    # Loop throuth the selected datasets
    for k in range(len(num)):
        ind = num[k]

        # Call global vars
        # ################
        run_check = eval(f"settings.run{ind}.get()")
        run_outl = eval(f"settings.bound{ind}.get()")
        outfolder = main_folder + f"/4_output/Data {ind}/{today}"

        if run_check ==1 and run_outl ==1:
            settings.erdlabel.config(text=f"Boundary/Constraint Check for Data{ind}")

            data_id = eval(f"settings.id_ent{ind}.get()")
            bound_vars = eval(f"settings.bound_id_ent{ind}.get('1.0', 'end-1c').replace('\\n','')")
            keep_vars = eval(f"settings.keep_ent{ind}.get().split(',')")
            bound_vars_list =  eval("bound_vars.split(',')")
            df = eval(f"settings.check_rawdata{ind}")
            print(bound_vars_list)

            # Generate neccesary output variables
            for i in ['bound_var_name', 'variable_ value', 'bound_message_']:
                keep_vars.append(i)
                df[i] = ''
            keep_vars.insert(0, data_id)  # Put Data ID as part of keep variables
            final_df = []  # Predefine the final outcome dataset
            df_cols = df.columns.tolist()
            for j in bound_vars_list:

                if j != '':
                    # Get variable name, lowerbound and upper bound
                    bound_var_ = j.split('|')[0]
                    bound_lower_ = j.split('|')[1]
                    bound_upper_ = j.split('|')[2]

                    # Ignore empty items
                    if bound_var_ in df_cols and is_numeric_dtype(df[bound_var_]):

                        df[bound_var_] = pd.to_numeric(df[bound_var_], downcast="float")

                        # Flag values lower than the lower bound
                        if bound_lower_ != '':
                            try:
                                bound_lower_ = float(bound_lower_)
                                df['bound_message_'] = np.where((df[bound_var_] < bound_lower_),
                                                                f"Value is less than the lower bound ({bound_lower_})", "")
                            except ValueError:
                                msg.showerror("Bound Check Error",
                                              f"Enter a valid numeric lower bound for {bound_var_} in Data {ind} ")
                        # Flag values higher than the upper bound
                        if bound_upper_ != '':
                            try:
                                bound_upper_ = float(bound_upper_)
                                df['bound_message_'] = np.where((df[bound_var_] > bound_upper_),
                                                                f"Value is greater than the upper bound ({bound_upper_})", df['bound_message_'])
                            except ValueError:
                                msg.showerror("Bound Check Error",
                                              f"Enter a valid numeric upper bound for {bound_var_} in Data {ind} ")
                                settings.erdlabel.grid_remove()


                        df['variable_ value'] = df[bound_var_]
                        df['bound_var_name'] = bound_var_
                        df_new = df[df['bound_message_'] != ""]
                        df_new = df_new[keep_vars]

                        final_df.append(df_new)
                    elif not is_numeric_dtype(df[bound_var_]):
                        msg.showerror("Bound check Error", f"{bound_var_} in Data {ind} is not a numeric variable\nCorrect that.")
                        pass
                        settings.erdlabel.grid_remove()
                    elif bound_var_ not in df_cols:
                        msg.showerror("Bound check Error", f"{bound_var_} not in Data {ind}. Please correct that")
                        pass
                        settings.erdlabel.grid_remove()
            final_df = pd.concat(final_df).reset_index()
            final_df = final_df[keep_vars]

            # Export to Excel
            mode = ''
            if Path(f'{outfolder}/Check_Output.xlsx').is_file():
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx', mode = 'a', if_sheet_exists='replace') as writer:
                    final_df.to_excel(writer, sheet_name='Boundary',index=False)
            else:
                with pd.ExcelWriter(f'{outfolder}/Check_Output.xlsx') as writer:
                    final_df.to_excel(writer, sheet_name='Boundary',index=False)

            settings.erdlabel.grid_remove()
