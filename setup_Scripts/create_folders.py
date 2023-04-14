

# ------------------------------------
# Name   : Create Folder Structure
# Purpose: Creates folder structure in a specific area
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
#-------------------------------------
import os
import sys
from tkinter import messagebox as msg
import settings

# Create folder system
def start():
    parent_folder = settings.parent_folder
    if parent_folder == "":
        msg.showwarning(title="Directory Error", message="Enter or Selct a valid location for the folders")
        #exit()
    else:
        # Create Archive folders 0_archive
        ##################################
        archive_folder = parent_folder + "/0_archive"
        if os.path.exists(archive_folder):
            f_info1 = "0_archive folder already exists: Skipped folder creation \n"
        else:
            os.makedirs(archive_folder)
            f_info1 = "0_archive folder created and populated \n"
        with open(archive_folder + '/0_readme.txt', 'w') as f:
            f.write("""This folder for storage of all archieves related to the data you are working on. \nYou may create subfolders to organize your files
            \nFor more information, contact the developer @ matthewglory1@gmail.com
             """)
            f.close()

        # Create Script folders 1_script
        ################################
        scripts_folder = parent_folder + "/1_scripts"
        if os.path.exists(scripts_folder):
            f_info2 = "1_scripts folder already exists: Skipped folder creation \n"
        else:
            os.makedirs(scripts_folder)
            f_info2 = "1_scripts folder created and populated \n"
        with open(scripts_folder + '/0_readme.txt', 'w') as f:
            f.write('''This folder for storage of all coding scripts related to the data you are working on. \nStore all coding scripts here
            \nFor more information, contact the developer @ matthewglory1@gmail.com
             ''')
            f.close()

        # Create Input folders 2_input
        ##############################
        input_folder = parent_folder + "/2_input"
        if os.path.exists(input_folder):
            f_info3 = "2_inputs folder already exists: Skipped folder creation \n"
        else:
            os.makedirs(input_folder)
            f_info3 = "2_inputs folder created and populated \n"
        with open(input_folder + '/0_readme.txt', 'w') as f:
            f.write("""This folder contains all the input files the program depends on to run. \nDo not move files out of this folder
            \nFor more information, contact the developer @ matthewglory1@gmail.com
             """)
            f.close()

        # Create Data folder folders
        ############################
        data_folder = parent_folder + "/3_data"
        if os.path.exists(data_folder):
            f_info4 = "3_data folder already exists: Skipped folder creation \n"
        else:
            os.makedirs(data_folder)
            f_info4 = "3_data folder created and populated \n"
        with open(data_folder + '/0_readme.txt', 'w') as f:
            f.write("""This folder for storage of all datasets you are working with. \nThe program will automatically pupulate the 3_clean folder
            \nFor more information, contact the developer @ matthewglory1@gmail.com
             """)
            f.close()

        # Create Preloads Data folder folders
        preload_folder = parent_folder + "/3_data/1_preloads"
        if os.path.exists(preload_folder):
            f_info5 = "3_data/1_preloads already exists: Skipped folder creation \n"
        else:
            os.makedirs(preload_folder)
            f_info5 = "3_data/1_preloads folder created and populated \n"

        # Create Raw Data folder folders
        raw_folder = parent_folder + "/3_data/2_raw"
        if os.path.exists(raw_folder):
            f_info6 = "3_data/2_raw already exists: Skipped folder creation \n"
        else:
            os.makedirs(raw_folder)
            f_info6 = "3_data/2_raw folder created and populated \n"

        # Create Clean Data folder folders
        clean_folder = parent_folder + "/3_data/3_clean"
        if os.path.exists(clean_folder):
            f_info7 = "3_data/3_clean already exists: Skipped folder creation \n"
        else:
            os.makedirs(clean_folder)
            f_info7 = "3_data/3_clean folder created and populated \n"


        # Create Output folder folders
        ##############################
        output_folder = parent_folder + "/4_output"
        if os.path.exists(output_folder):
            f_info8 = "4_output already exists: Skipped folder creation \n"
        else:
            os.makedirs(output_folder)
            f_info8 = "4_output folder created and populated \n"
        with open(output_folder + '/0_readme.txt', 'w') as f:
            f.write("""This folder stores all output files. \nThe program will automatically pupulate this folder
            \nFor more information, contact the developer @ matthewglory1@gmail.com
             """)
            f.close()

        # Create Report folder folders
        ###############################
        report_folder = parent_folder + "/5_report"
        if os.path.exists(report_folder):
            f_info9 = "5_report already exists: Skipped folder creation \n"
        else:
            os.makedirs(report_folder)
            f_info9 = "5_report folder created and populated \n"
        with open(report_folder + '/0_readme.txt', 'w') as f:
            f.write("""You can log any report or documentation on the data here.""")
            f.close()

        # Create Media folder folders
        #############################
        media_folder = parent_folder + "/6_media"
        if os.path.exists(media_folder):
            f_info10 = "6_media already exists: Skipped folder creation \n"
        else:
            os.makedirs(media_folder)
            f_info10 = "6_media folder created and populated \n"
        with open(media_folder + '/0_readme.txt', 'w') as f:
            f.write("""Keep all media files related to the data here.""")
            f.close()
        # Create Audio folder folders
        audio_folder = parent_folder + "/6_media/1_audio"
        if os.path.exists(audio_folder):
            f_info11 = "6_media/1_audio already exists: Skipped folder creation \n"
        else:
            os.makedirs(audio_folder)
            f_info11 = "6_media/1_audio folder created and populated \n"
        # Create Video folder folders
        video_folder = parent_folder + "/6_media/2_video"
        if os.path.exists(video_folder):
            f_info12 = "6_media/2_video already exists: Skipped folder creation"
        else:
            os.makedirs(video_folder)
            f_info12 = "6_media/2_video folder created and populated"

        # Folder creation note
        creat_note = f_info1 + f_info2 + f_info3 + f_info4 + f_info5 + f_info6 + f_info7 + f_info8 + f_info9 + \
                     f_info10 + f_info11 + f_info12
        msg.showinfo("Complete", creat_note)

        # Update global variables
        #########################
        settings.archive_folder = archive_folder
        settings.scripts_folder = scripts_folder
        settings.input_folder = input_folder
        settings.data_folder = data_folder
        settings.preload_folder = preload_folder
        settings.raw_folder = raw_folder
        settings.clean_folder = clean_folder
        settings.output_folder = output_folder
        settings.report_folder = report_folder
        settings.media_folder = media_folder
        settings.audio_folder = audio_folder
        settings.video_folder = video_folder
