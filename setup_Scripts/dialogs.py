# ------------------------------------
# Name   : Dialog Boxed
# Purpose: Functions for dialog boxes
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
#-------------------------------------

import os
from tkinter import filedialog as fd
from tkinter import messagebox as msg

import settings


# Function to select folders
def get_folder():
    # root.wm_attributes('-topmost', 1)
    global f_dir
    f_dir = fd.askdirectory(
        title='Open a file',
        initialdir='/')
    f_dir = str(f_dir)
    settings.folder_name = f_dir
    #pa_folder.insert(0, settings.folder_name)
    #root.update()
    return f_dir


# Function to select files
def get_file(fname):
    settings.fname = fname
    global r_file
    filetypes = (
        ('All files', '*.*'),
        ('Excel', ['*.xlsx', '*.xls', '*.csv']),
        ('Stata', '*.dta'),
        ('All files', '*.*')
    )
    r_file = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    r_file = str(r_file)
    r_file_name = os.path.basename(r_file)


    if (fname == "xfile1"):
        settings.raw_file1 = r_file
        settings.x_file1_ent = r_file_name
    elif (fname == "dfile1"):
        #settings.filenum = '1'
        settings.raw_data_file1 = r_file
        settings.d_file1_ent = r_file_name
    elif (fname == "xfile2"):
        settings.raw_file2 = r_file
        settings.x_file2_ent = r_file_name
    elif (fname == "dfile2"):
        settings.raw_data_file2 = r_file
        settings.d_file2_ent = r_file_name
    elif (fname == "xfile3"):
        settings.raw_file3 = r_file
        settings.x_file3_ent = r_file_name
    elif (fname == "dfile3"):
        settings.raw_data_file3 = r_file
        settings.d_file3_ent = r_file_name
    elif (fname == "xfile4"):
        settings.raw_file4 = r_file
        settings.x_file4_ent = r_file_name
    elif (fname == "dfile4"):
        settings.raw_data_file4 = r_file
        settings.d_file4_ent = r_file_name
    elif (fname == "xfile5"):
        settings.raw_file5 = r_file
        settings.x_file5_ent = r_file_name
    elif (fname == "dfile5"):
        settings.raw_data_file5 = r_file
        settings.d_file5_ent = r_file_name
    elif (fname[0:8] == "checkraw"):
        fnum = fname[-1]
        settings.check_raw_sel = r_file
        settings.check_raw_ent = r_file_name
        exec("settings.check_raw" + fnum + "= r_file")
    elif fname == "dfile":
        settings.fname = r_file


    #msg.showinfo(r_file, settings.fname)
