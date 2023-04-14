'''
##############################
Date: Jan 2023
@author: Mathew Bidinlib
Purpose: STS DB info
###############################
'''
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit_authenticator as stauth
import plotly_express as px
import numpy as np
from PIL import Image



# Set page outline and footer
st. set_page_config(layout="wide")

# Set the footer
footer="""<style>
a:link , a:visited{
color: #D891FC;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a href="https://www.github.com/mbidinlib/" target="_blank">Developer </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

   
header2 =  st.markdown("""<h2 style = "font-size:30px ; font-family: Tahoma; 
                        color: #FFFFFF;text-align:center; background-color:#035454">
                        PRC DATA CHECK SYSTEM</h2> """,unsafe_allow_html=True)

# Write overview in columns
col1, col2= st.columns((1.5,4)) #Split into two columns
# Total ConsultantsGender
with col1:
    st.markdown(f''' <h3 style = "font-size:20px ; font-family: 'Cooper Black'; 
                color: #FFFFFF; background-color:#313868; text-align: center">
                   </h3>''', unsafe_allow_html=True)
    st.markdown(f''' <h3 style = "font-size:20px ; font-family: 'Cooper Black'; 
                color: #FFFFFF; background-color:#313868; text-align: center">
                Download App </h3>''', unsafe_allow_html=True)
    st.markdown("")        

    exe02 = open("st_exe/PRC Data Check.exe", "rb")
    st.download_button(label='Click herer to download \n the latest version(0.2)', 
                       data=exe02, file_name='PRC Data Check_v0.2.exe')
    st.markdown("""<u><h5 style= "color: #FFFFFF; background-color:#313868; text-align: left">Latest Version 0.2</u>
                \n <font color = "#F304E8">Release Date: Feb 27, 2023 </font> 
                \nImprovements includes<br>
                <li>Optimized Attachment download for SurveyCTO</li>
                <li>Fixed bug in downloading CSV for SurveyCTO</li>
                <li>Fixed missing values issues with SurveyCTO Downloads</li>
                """,unsafe_allow_html=True)          
    
# Gender
with col2:

    st.markdown("")        
    st.markdown("""<h3 style= 'text-align: center'> User Guide</h3>""",unsafe_allow_html=True)        

    st.markdown(f''' <h3 style = "font-size:30px ; font-family: 'Tahoma'; color: #FFFFFF;
                background-color:#039DA7;text-align: center">
                1. Introduction </h3>''', unsafe_allow_html=True)
    st.markdown("")        
    st.markdown("""<h5 style= 'text-align: left'>PRC Data Check System (PRCDC) is a Python based 
                data engineering system for checking and processing data. The system leverages on GUI 
                models in Python to make interacting and checking of data easy and quick without prior 
                coding experience. The app currently comes with three main functionalities namely the 
                API data download, data dictionary for ODK related surveys and general data checks. 
                The figure below shows an overview of the system.</h5>""",unsafe_allow_html=True)      
    int_image = Image.open('st_images/intro_picture.jpg')
    st.image(int_image, caption='Overview of PRCDC')  
    st.markdown("")          
    st.markdown("")        

    #   Section 2
    ##################
    st.markdown(f''' <h3 style = "font-size:30px ; font-family: 'Tahoma'; color: #FFFFFF;
                background-color:#039DA7;text-align: center">
                2. API Data Download </h3>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>The API download functionality allows users conducting surveys 
                with ODK related platforms to download data at a faster pace with just a click of a button. 
                While the download currently supports only the SurveyCTO based surveys, future versions would 
                include downloading from other survey-related platforms. For this to work, users need to allow 
                API access on their server.</h5>""",unsafe_allow_html=True)      
    st.markdown(f''' <i><h4 style = "font-size:20px ; font-family: 'Tahoma';text-align: Left">
                2.1 Downloading from SurveyCTO API </h4> </i>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>SurveyCTO users can now download data at a fast pace with this 
                functionality. The download duration ranges between 10 seconds to 10 minutes depending on the 
                size of the data and volume of attachments. Select SurveyCTO and enter the parameters as seen 
                below.</h5>""",unsafe_allow_html=True)      
    api_image1 = Image.open('st_images/api_picture_1.jpg')
    st.image(api_image1, caption='')  
    st.markdown("""<h5 style= 'text-align: left'>The varioius paremeters are explained in the table below.</h5>""",unsafe_allow_html=True)      
    api_image2 = Image.open('st_images/api_picture_2.jpg')
    st.image(api_image2, caption='')  
    st.markdown("""<h5 style= 'text-align: left'>The blue download button would initiate the download with the 
                dataset download first, followed by attachments where applicable. The downloaded dataset would 
                come in CSV format and names with the form id specified. It currently allows only wide format 
                downloads. When the download is triggered and attachments enabled, a cancel button would be 
                displayed below to enable cancellation when the user wishes to </h5>""",unsafe_allow_html=True)      
    st.markdown("")        
    st.markdown("")        



    #   Section 3
    ##################
    st.markdown(f''' <h3 style = "font-size:30px ; font-family: 'Tahoma'; color: #FFFFFF;
                background-color:#039DA7;text-align: center">
                3. Generating Data Dictionaries</h3>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>This functionality allows users who program their survey forms 
                with xls forms to generate a python dictionary of choice lists for their dataset. This 
                dictionary may be used to import that data into Stata or SPSS forms that have the actual 
                choice values and labels. You can generate dictionaries for up to 5 projects/surveys at a 
                time.</h5>""",unsafe_allow_html=True)      
    st.markdown(f''' <i><h4 style = "font-size:20px ; font-family: 'Tahoma';text-align: Left">
                3.1 Generating Dictionaries </h4> </i>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>
                1. Select the xls and their corresponding datasets at the left side of the home page as seen below
                Datasets are required only when the user wants to produce a data output. For only scripts, users may select only the xls forms.
                </h5>""",unsafe_allow_html=True)      
    dict_image1 = Image.open('st_images/dict_picture_1.jpg')
    st.image(dict_image1, caption='')  
    st.markdown("""<h5 style= 'text-align: left'>
                Datasets are required only when the user wants to produce a data output. For only scripts, users may select only the xls forms.
                </h5>""",unsafe_allow_html=True)      
    st.markdown("""<p><h5 style= 'text-align: left'>
               2.	Select the parent folder where you would like to store the scripts.The parent folder should 
               be in PRCDC format. If you don’t have such folder structure, use the setup folder structure 
               section to create the folder structure.
                </h5>""",unsafe_allow_html=True)      
    dict_image2 = Image.open('st_images/dict_picture_2.jpg')
    st.image(dict_image2, caption='')  
    st.markdown("""<p><h5 style= 'text-align: left'>
                Datasets are required only when the user wants to produce a data output. For only scripts, users may select only the xls forms.
                </h5></p>""",unsafe_allow_html=True)      
    st.markdown("""<p><h5 style= 'text-align: left'>
               3.	Click on generate dictionary button and the final scrips would be stored 
               in the <u><i>1_scripts subfolder</i></u>.
                </h5>""",unsafe_allow_html=True)      
    st.markdown("")        
    st.markdown("")        




    #   Section 4
    ##################
    st.markdown(f''' <h3 style = "font-size:30px ; font-family: 'Tahoma'; color: #FFFFFF;
                background-color:#039DA7;text-align: center">
                4. Checking Data</h3>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>The data check section allows users the opportunity to check 
                for issues and inconsistencies. The section comes with three different functionalities namely 
                a) setup b) checks c) session control.</h5>""",unsafe_allow_html=True)      
    
    st.markdown(f''' <i><h4 style = "font-size:20px ; font-family: 'Tahoma';text-align: Left">
                4.1 Setup </h4> </i>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>
                The setup functionality is used to set the necessary checks that the user may want to run on 
                the datasets. This section allows up to 5 datasets per session with a <i>multiple session</i> 
                functionality powered by the session control (see section 4.3).
                </h5>""",unsafe_allow_html=True)      
    st.markdown("""<h5 style= 'text-align: left'>
                Datasets are required only when the user wants to produce a data output. For only scripts, users may select only the xls forms.
                </h5>""",unsafe_allow_html=True)      
    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.1.1 Preliminary Setups</i> <br> 
                This is where you import your datasets and choose necessary variables including unique identifiers
                and variables to keep. You also get to choose which datasets you wish to run checks on, and 
                which checks you wish to run at each time. There are seven (7) simple steps to complete the preliminary setups.
                <ol type = "a">
                <li>Select the number of datasets: As shown in the flow diagram below, you get to choose the number of 
                datasets for the session/project. The maximum allowed per section is 5. Based on the number selected, rows would 
                be created for selection of datasets. You do not need this if you are checking only one dataset, since the default is 1. 
                </li>
                <li>Select a dataset for each row: For each of the rows created (based on the number selected in a), you would click 
                the button to select the excel or CVS dataset. The actual name of the selected data would be displayed in the textbox at 
                the bottom to help the user identify the dataset and verify if the right data is selected. You can always replace the 
                selected dataset by selecting a new one.
                </li>
                <li>Select the unique identifier:  When a valid dataset is selected, a button for selecting the unique identifier 
                (ID) appears. Click to select the ID for each dataset. 
                </li>
                <li>Select the variables to keep in outputs: Use this button to select the key variables you would like to see for each 
                observation that is flagged by the checks. Click to add a variable until you have your desired key variables.
                </li>
                <li>Activate each dataset for check: The check boxes in the section called Select dataset to check would then be needed to 
                activate each dataset for checks at every time. This is an on-off button that can be changed anytime based on the user’s preferences. 
                </li>
                <li>Activate each individual check: When a dataset is activated for checks, the check boxes for the individual checks at the 
                right side would be activated for use. Turn on all check that you would like to setup and run. These are on-off buttons that can 
                be changed based on the user’s preference.
                </li>
                <li>Update entries for checks: Click the blue button at the button of the check boxes labeled “Update” to update field for setting 
                up the checks. When the button is pressed, the spaces for the various checks at the right side would be populated with fields to setup 
                variables and parameters for checks.
                </li> </ol>
                The flow diagram below demonstrates the steps in completing the preliminary setup.                
                </h5>""",unsafe_allow_html=True)     
    dict_image1 = Image.open('st_images/checks_setup_picture1.jpg')
    st.image(dict_image1, caption='')  
 
    st.markdown(f''' <i><h4 style = "font-size:20px ; font-family: 'Tahoma';text-align: Left">
                4.2 Checks</h4> </i>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>
                Having activated the variables/parameters fields, you now proceed to setup each check for all datasets that were activated. 
                The various checks are explained in the sections following:</h5>""",unsafe_allow_html=True)      
    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.1.1 Check for Duplicates</i> <br> 
                This check is easy to setup and requires you to select only the unique identifier variable(s) you would like use to check for duplicates. 
                The unique identifiers selected in previous sections would be prefilled here automatically. You don’t need to do any extra work if you wish 
                to check duplicates on these variables. Otherwise, select the combination of variables that uniquely identify the dataset. Multiple selection 
                is allowed here for combination of variables that uniquely identify the dataset. You may also type or paste a comma separated list of variables. 
                For the example below, Dataset 1 has one variable that uniquely identifies the dataset <i>(caseid_f)</i> while Dataset 2 has 2 and so on…                  
                </h5>""",unsafe_allow_html=True)
    dict_image1 = Image.open('st_images/duplicates_picture.jpg')
    st.image(dict_image1, caption='')  
    
    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.2.2 Check for Missing Values</i> <br> 
                With this check, you will select all the variables that you wish to check for missing values for each dataset. You can also type or past a coma 
                separated list of variables for each dataset. The diagram below shows an example of missing checks setup for Datasets 1, 2 and 3                
                </h5>""",unsafe_allow_html=True)
    dict_image1 = Image.open('st_images/missing_picture.jpg')
    st.image(dict_image1, caption='')  

    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.2.3 Check for outliers</i> <br> 
                For this check, you will select all the <u>numeric variables</u> you wish to check for outliers for each dataset. You can also type or past a coma 
                separated list of numeric variables for each dataset. The diagram below shows an example of outlier checks setup for all datasets.                
                </h5>""",unsafe_allow_html=True)
    dict_image1 = Image.open('st_images/outlier_picture.jpg')
    st.image(dict_image1, caption='')  

    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.2.4 Other-Specify Exports</i> <br> 
                This check helps users conducting surveys to export variables where respondents specify other values. 
                You will select a pair of categorical parent and child variables and click the button below to add them. 
                The parent variable is the categorical survey question that has other-specify in the list and the child is the variable where the other is specified. 
                You may also type a pair of parent and child variables separated by a pipe (|) <u><tt>parent1|child1, parent2|child2</tt></u>. 
                Each pair is distinguished by a comma. The image below shows a sample setup.
                </h5>""",unsafe_allow_html=True)
    dict_image1 = Image.open('st_images/otherspecify_picture.jpg')
    st.image(dict_image1, caption='')  

    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.2.5 Boundary/Constraint Checks</i> <br> 
                This check is used to flag values that are not within a certain range or boundary, by specifying the lower and upper boundary for each variable you want to check. 
                You will select a numeric variable, enter the upper and lower boundaries and click the button below to add that variable to the list. 
                For those who want to quickly type in, you may type the list as with each variable having the lower and upper separated by a pipe(|) as follows; 
                <u><tt>var1|lower|upper, var2|lower|upper, var3|lower|upper</u></tt>. Note that each variable and boundary items is separated by a comma. The image below is a sample boundary check setup.
                </h5>""",unsafe_allow_html=True)
    dict_image1 = Image.open('st_images/boundary_picture.jpg')
    st.image(dict_image1, caption='')  


    st.markdown(f''' <i><h4 style = "font-size:20px ; font-family: 'Tahoma';text-align: Left">
                4.3 Session control</h4> </i>''', unsafe_allow_html=True)
    st.markdown("""<h5 style= 'text-align: left'>
                Seeing that all the checks could take a couple of minutes and one would not want to repeat the process everything you reopen the app, the developer adds this section to 
                allow users save current settings to a location and reopen it whenever one wishes. This is also helpful for collaborative work where teams would like to all have access to 
                the same settings and anyone could run the checks anytime. The saved file may be stored in the folder created by the system and shared with teams.
                Session control also helps setup multiple projects and navigate between projects.
                </h5>""",unsafe_allow_html=True)      
    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.3.1 Session save</i> <br> 
                Select the first option from the session control, select the location where you would like to save the session 
                and the name of the session/project. Click the run button the save the session.                
                </h5>""",unsafe_allow_html=True)
    ss_image1 = Image.open('st_images/session_picture_1.jpg')
    st.image(ss_image1, caption='')  
    
    st.markdown("""<p><h5 style= 'text-align: left'> <i>4.3.2 Session Restore</i> <br> 
                To restore a previous session or project, select Restore session and select the location of the saved session 
                All previously saved sessions would be populated at the name session for selection. Select the appropriate project/session and click run. 
                As seen below:</h5>""",unsafe_allow_html=True)
    ss_image2 = Image.open('st_images/session_picture_2.jpg')
    st.image(ss_image2, caption='')  
    st.markdown("""<p><h5 style= 'text-align: left'> 
                The session restore would update the app with all the datasets, selected variables and settings that were done at the point of restoration. Users can easily switch between projects 
                using the session restore function.
                </h5>""",unsafe_allow_html=True)
