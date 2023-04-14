# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Preserves and restores progress
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
# -------------------------------------

# imports
import json
import settings
from tkinter import messagebox as msg

# Control variables
session_folder = "C:/PRC_folder"
session_file = "sample" + ".json"
all_vars_n = settings.all_var_names_norm
all_vars_g = settings.all_var_names_get
all_vars_gg = settings.all_var_names_gett

all_vars = all_vars_n + all_vars_g + all_vars_gg

def run_session_control(s_type, folder,file,version):

    if s_type == 'Save_session' and file != '':

        previous_session= {}
        # Loop through variable names and append in dictionary
        for k in all_vars_n:
            val = eval(f'settings.{k}')
            previous_session[k] = str(val)

       #  Entry and combo-box variables
        for k in all_vars_g:
            # Get values from widgets
            if 'r_' in k:
                vn = k.split('_')[1]
            else:
                vn = k
            try:
                val = eval(f'settings.{vn}.get()')
                previous_session[k] = str(val)
            except:
                 previous_session[k] = ""

        # Text variables
        for k in all_vars_gg:
            try:
                val = eval(f"settings.{k}.get('1.0', 'end-1c')")
                previous_session[k] = str(val)
            except:
                  previous_session[k] = ""

        print(previous_session)
        print( s_type, folder,file,version)

        # Save Session in a json file
        json_object = json.dumps(previous_session, indent=10)

        # Writing to sample.json
        with open(folder + "/" + file + '.json', "w") as outfile:
            outfile.write(json_object)

        msg.showinfo("Success", "This session has been successfully saved.")


    if s_type=='Restore Session' and file != '':
        # Restore session
        # ################
        # Open file
        with open(folder + "/" + file + '.json', "r") as outfile:
            # Reading from json file
            restored = json.load(outfile)

        # restore values
        for i in all_vars:
            if 'keep_ent' in i or 'id_ent' in i:
                j = 'r_' + i
                exec(f"settings.{j} = restored['{i}']")
            else:
                exec(f"settings.{i} = restored['{i}']")
            # print(f"settings.{i}==:", eval(f"settings.{i}"))





