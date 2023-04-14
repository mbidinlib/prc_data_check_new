# -*- coding: UTF-8 -*-
# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Creates data dictionaries for
#          data downloaded in scto
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
#-------------------------------------

import pandas as pd
import numpy as np
import openpyxl
import sys
import os
from datetime import date, datetime
from tkinter import messagebox as msg
import tkinter as tk

import settings

# Start import script
# ********************

def gen_dict_files():
    main_folder = settings.main_folder
    script_folder = main_folder + "/1_scripts"
    rawdata_folder = main_folder + "/3_data/2_raw"
    clean_folder = settings.main_folder + "/3_data/3_clean"
    today = datetime.now()
    today = today.strftime("%d/%m/%Y %H:%M:%S")

    scripts_count = int(settings.num_raw_files)
    create_message = 'The following Scripts were generated:\n'
    valid = 0
    for i in range(1,scripts_count+1):

        xls_file = eval("settings.raw_file" + str(i))
        raw_data_name = eval("settings.raw_data_file" + str(i))

        # Get actual file names
        x_name = os.path.basename(xls_file)
        xls_name = os.path.splitext(x_name)[0]  # # file name without extension
        r_name = os.path.basename(raw_data_name)
        raw_name = os.path.splitext(r_name)[0]  # # file name without extension

        # Raise a warning if an xls file is not selected

        if (xls_name == ""):
            erlabel = tk.Label(settings.dict_frame,
                             text= f"There is no file selected for xls file {i}\n the program will skip # {1}",
                             background="red",
                             foreground="white",font=('Airial', 20, "bold"))
            erlabel.grid(row=32, column=0, columnspan=5)
            erlabel.after(10000, erlabel.destroy)

        else:
            script_name = script_folder + "/" + xls_name + '.py'
            # """
            script_out = open(script_name, 'w')
            script_out.write(
            '# -*- coding: UTF-8 -*- \n' 
            '# ---------------------------------------------\n'
            '# Name   : Data Dictionary                       \n'
            '# Purpose: Creates SCTO dictionary for raw data   \n'
            f'# Date :    {today}                                \n'
            '# Developer : Mathew Bidinlib                       \n'
            '# Email  : matthewglory1@gmail.com                   \n'
            '# Contact: +1 901 568 7871                            \n'
            '#------------------------------------------------      \n'
            '                                                        \n'
            'import pandas as pd                                       \n'
            'import openpyxl                                         \n\n\n'
            '# Import Raw Data                                             \n'
            f'raw_data = pd.read_csv("{raw_data_name}")\n\n'
            )

            # Import sheets
            cwd = os.getcwd()

            xls_choice = pd.read_excel(xls_file, sheet_name="choices")
            xls_survey = pd.read_excel(xls_file, sheet_name="survey")

            # Create a dictionary of all choices
            xls_survey['repeats'] = ""
            choices = xls_choice[xls_choice['list_name'].notna()]
            choice_names = choices['list_name']
            choice_values = choices['value']
            choice_labels = choices['label']

            # Survey Questions and their choice setups
            ###########################################
            survey = xls_survey[xls_survey['type'].notna()]
            cat_rows = survey[survey['type'].str.contains('select_one|repeat')]                                                     # Pick rows with select one
            # Indexes of all begin repeat and end repeat rows
            beg_rep_ind = survey.index[survey['type'].str.contains('begin repeat')].tolist()
            end_rep_ind = survey.index[survey['type'].str.contains('end repeat')].tolist()

            # Check for categorical variables within a repeat group
            iter = 0
            for k in range(1, len(beg_rep_ind)+1):
                iter = iter + 1
                beg_val = beg_rep_ind[k-1]
                end_val = end_rep_ind[k-1]
                cat_rows.loc[(cat_rows.index > beg_val) & (cat_rows.index < end_val), 'repeats'] = "Yes"
            cat_rows.loc[cat_rows['repeats'] == "Yes", 'name'] = cat_rows['name'] + '_1'
            cat_rows['type'] = cat_rows['type'].str.replace('select_one ', '',regex=True)
            cat_names = cat_rows[['type', 'name']]


            # Get Categorical choices
            names = choice_names.unique()
            for i in names:
                # Variables that have the choice list
                cat_vars = cat_names.loc[cat_names['type'] == i , 'name'].tolist()
                lists = choices[choices['list_name'] == f'{i}']
                vals_len = len(lists)

                # Create a dictionary for each unique item on the choices sheet
                # =============================================================
                dict = ""
                for j in range(1,vals_len+1):
                    lab = lists['label'].iloc[j-1]                                                                           #Choice value for the jth element
                    val = lists['value'].iloc[j-1]                                                                           #Choice label for the jth element
                    try:
                        lab = bytes(lab, 'utf-8').decode('utf-8', 'ignore').strip().replace("\n"," ")                            # Remove non-utf8 characters from the labels
                    except:
                        lab = lab
                    # Check values that are string and stringify their values in the dictionary
                    if type(val) == str:
                        stad = '"'
                    else:
                        stad = ''
                    # Define each element in the dictionary
                    if j == 1:
                        dict = dict + '\n  ' f'{stad}{val}{stad} : "{lab}"'
                    else:
                        dict = dict + ',\n  ' f'{stad}{val}{stad} : "{lab}"'

                choice_name = i
                # Check for and change conflicting choice names
                if i == 'class' or i == 'def':
                    i = i + "_dictionary"

                # Write dictionary to script
                var_dic = f'{i}_variables'
                out_data = clean_folder + "/" + raw_name + '_cat.xlsx'
                out_stata = clean_folder + "/" + raw_name + '_cat.dta'

                if i != "nan" and len(cat_vars) >= 1:
                    script_out.write(
                    f'# Dictionary for categorical variables with [{i}] choices\n'
                    f'{var_dic} = {cat_vars}\n'
                    f'{i}' + ' = {' + f'{dict}' + ' \n  }\n\n')

                        # Write the code that applies the dictionary to the data\
                    script_out.write(
                        '# Map Columns to Dictionary \n'
                        f'for j in {var_dic}:\n'
                        '  raw_data.replace({ j' + f' : {i}' + ' },inplace=True)\n'
                        f'  raw_data[j] = raw_data[j].astype("category")\n'
                    )

                # Import Raw data and apply Script to data
                if raw_data_name == "":
                    erlabel = tk.Label(settings.dict_frame,
                                       text=f"There is no file selected for data file {i}\n the program will not apply categorical dictionary to data # {1}",
                                       background="red",
                                       foreground="white", font=('Airial', 20, "bold"))
                    erlabel.grid(row=32, column=0, columnspan=5)
                    erlabel.after(10000, erlabel.destroy)

                else:
                    raw_data = pd.read_csv(raw_data_name)
                    if i != "nan" and len(cat_vars) >= 1:
                        app_vars = cat_vars
                        app_dict = eval('{' + dict + '}')
                        for var in app_vars:
                            raw_data.replace({var: app_dict}, inplace=True)
                            raw_data[var] = raw_data[var].astype("category")

            # Export data and close script
            script_out.write(
                f'raw_data.to_excel("{out_data}", index=False)\n'
                f'raw_data.to_stata("{out_stata}", version=118 , write_index=False)\n\n'

            )
            script_out.close()

            # Apply Dictionary to columns
            if raw_data_name != "":
                raw_data.to_excel(out_data, index=False)
                raw_data.to_stata(out_stata, version=118, write_index=False)
            # Flag rows that don't have a selected raw data
            valid += 1
            create_message = create_message + "\n" + xls_name + ".py"
    if valid > 0 :
        msg.showinfo('Dictionary Scripts', create_message + "\n\n Location: \n" + script_folder)
    else:
        msg.showinfo('No Output',"No output generated. Select valid files for xls amd data files")

        # """
#os.system(script_name)

