# ------------------------------------
# Name   : PRC DataCheck Setup Script
# Purpose: Sets Global variables
# Author : Mathew Bidinlib
# Email  : matthewglory1@gmail.com
# -------------------------------------

def gloSettings():

    global f_location, location , parent_folder, archive_folder, scripts_folder, input_folder,\
               data_folder, preload_folder, raw_folder, clean_folder, output_folder, report_folder,\
               media_folder, audio_folder, video_folder, raw_file1, raw_file2, raw_file3, raw_file4, raw_file5, \
               raw_data_file1, raw_data_file2, raw_data_file3, raw_data_file4, raw_data_file5, \
               fname, folder_name, main_folder, num_raw_files, x_file1_ent, x_file2_ent, x_file3_ent, \
               x_file4_ent, x_file5_ent, d_file1_ent, d_file2_ent, d_file3_ent, d_file4_ent, d_file5_ent, filenum, \
               inp_file_sel, inp_file_ent, num_data_files, check_raw_ent, check_rawdata1 , check_rawdata2 , check_rawdata3 \
              , check_rawdata4 , check_rawdata5 , check_raw1 , check_raw2 , check_raw3 , check_raw4 , check_raw5, \
               checks_id1, checks_id2, checks_id3, checks_id4, checks_id5, run1, run2, run3, run4, run5, \
               ckb1, ckb2, ckb3, ckb4, ckb5, dup1, miss1, outl1, other1, bound1, visu1,dup2,miss2, outl2, other2, bound2, visu2, \
               dup3,miss3, outl3, other3, bound3, visu3,dup4, miss4, outl4, other4, bound4, visu4,dup5, miss5, outl5, other5, bound5, visu5, \
               dp1, ms1, ol1, ot1, tb1, vs1, dp2, ms2, ol2, ot2, tb2, vs2, dp3, ms3, ol3, ot3, tb3, vs3,checks_fame, \
              dp4, ms4, ol4, ot4, tb4, vs4, dp5, ms5, ol5, ot5, tb5, vs5, dupn1, dupn2, dupn3, dupn4, dupn5, \
              dup_id_ent1, dup_id_ent2, dup_id_ent3, dup_id_ent4, dup_id_var5, dpsel1 , dpsel2 , dpsel3 , dpsel4 , dpsel5, \
              missn1, missn2, missn3, missn4, missn5, \
              miss_id_ent1, miss_id_ent2, miss_id_ent3, miss_id_ent4, miss_id_var5, \
             outln1, outln2, outln3, outln4, outln5, \
             outl_id_ent1, outl_id_ent2, outl_id_ent3, outl_id_ent4, outl_id_var5, \
             othern1, othern2, othern3, othern4, othern5, \
             other_id_ent1, other_id_ent2, other_id_ent3, other_id_ent4, other_id_var5,  \
             boundn1, boundn2, boundn3, boundn4, boundn5, \
             bound_id_ent1, bound_id_ent2, bound_id_ent3, bound_id_ent4, bound_id_var5, \
             tabun1, tabun2, tabun3, tabun4, tabun5, \
             tabu_id_ent1, tabu_id_ent2, tabu_id_ent3, tabu_id_ent4, tabu_id_var5, \
             keep_ent1, keepsel1, keep_ent2, keepsel2, keep_ent3, keepsel3, keep_ent4, keepsel4, keep_ent5, keepsel5, \
             id_ent1, id_ent2, id_ent3, id_ent4, id_ent5, erdlabel,session_type, session_folder, session_file, session_version , \
             sel_frame, abort, a_links, attach_folder , scto_user, scto_pass, pb, value_label, server_conn, action_label, \
             curr_att











    # Declare initial global variables
    parent_folder = '' ;    location = ''
    archive_folder = '' ;   scripts_folder = ''  ;  input_folder = ''
    data_folder = ''    ;   preload_folder = ''  ;   raw_folder = ''
    clean_folder = ''   ;    output_folder = ''  ;   report_folder = ''
    media_folder = ''   ;    audio_folder = ''   ;   video_folder = ''
    raw_file1 = ''      ;    raw_file2 = ''      ;    raw_file3 = ''
    raw_file4 = ''      ;    raw_file5 = ''      ;  raw_data_file1 = ''
    raw_data_file2 = '' ;    raw_data_file3 = ''  ;  raw_data_file4 = ''
    raw_data_file5 = '' ;    fname = ''           ;  folder_name = ''
    main_folder    = '' ;    num_raw_files = 0   ;  filenum = ''
    x_file1_ent = ''    ;    x_file2_ent = ''      ;  x_file3_ent = ''
    x_file4_ent = ''    ;    x_file5_ent = ''      ;  d_file1_ent = ''
    d_file2_ent = ''    ;    d_file3_ent = ''      ;  d_file4_ent = ''
    d_file5_ent = ''    ;   dict_frame = ''        ; inp_file_sel = ''
    inp_file_ent = ''   ;   num_data_files = 0      ; check_raw_ent= ''
    check_rawdata1 =''  ;   check_rawdata2 =''  ;     check_rawdata3 =''  ;
    check_rawdata4 =''  ;   check_rawdata5 =''  ;     check_raw1 = ''  ;
    check_raw2 = '';        check_raw3 = ''  ;         check_raw4 = ''  ;
    check_raw5 = ''     ;   checks_id1 = ''     ;      checks_id2 = ''     ;
    checks_id3 = ''     ;   checks_id4 = ''     ;      checks_id5 = ''     ;
    run1 = 0 ; run2=0 ;   run3 =0 ; run4 =0     ;       run5 = 0    ;
    ckb1 = "" ;   ckb2 = ""  ; ckb3 = ""     ; ckb4 =  "" ;     ckb5 = "";
    dup1 = 0 ; miss1 = 0 ;  outl1 = 0 ; other1=0; bound1=0; tabu1=0;
    dup2 = 0 ; miss2 = 0 ;  outl2 = 0 ; other2=0; bound2=0; tabu2=0;
    dup3 = 0 ; miss3 = 0 ;  outl3 = 0 ; other3=0; bound3=0; tabu3=0;
    dup4 = 0 ; miss4 = 0 ;  outl4 = 0 ; other4=0; bound4=0; tabu4=0;
    dup5 = 0 ; miss5 = 0 ;  outl5 = 0 ; other5=0; bound5=0; tabu5=0;
    r_dup1 = 0 ; r_miss1 = 0 ;  r_outl1 = 0 ; r_other1=0; r_bound1=0; r_tabu1=0;
    r_dup2 = 0 ; r_miss2 = 0 ;  r_outl2 = 0 ; r_other2=0; r_bound2=0; r_tabu2=0;
    r_dup3 = 0 ; r_miss3 = 0 ;  r_outl3 = 0 ; r_other3=0; r_bound3=0; r_tabu3=0;
    r_dup4 = 0 ; r_miss4 = 0 ;  r_outl4 = 0 ; r_other4=0; r_bound4=0; r_tabu4=0;
    r_dup5 = 0 ; r_miss5 = 0 ;  r_outl5 = 0 ; r_other5=0; r_bound5=0; r_tabu5=0;
    dp1 = "" ; ms1 = '' ;  ol1 = '' ; ot1=''; tb1=''; vs1='';
    dp2 = "" ; ms2 = '' ;  ol2 = '' ; ot2=''; tb2=''; vs2='';
    dp3 = "" ; ms3 = '' ;  ol3 = '' ; ot3=''; tb3=''; vs3='';
    dp4 = "" ; ms4 = '' ;  ol4 = '' ; ot4=''; tb4=''; vs4='';
    dp5 = "" ; ms5 = '' ;  ol5 = '' ; ot5=''; tb5=''; vs5='';
    dupn1 = ''; dupn2 = ''; dupn3 = ''; dupn4 = ''; dupn5 = '';
    dup_id_ent1 = ''; dup_id_ent2 = ''; dup_id_ent3 = ''; dup_id_ent4 = ''; dup_id_ent5 = '';
    dpsel1 = '' ; dpsel2 = ''; dpsel3 = ''; dpsel4 = '';dpsel5 = ''
    missn1 = ''; missn2 = ''; missn3 = ''; missn4 = ''; missn5 = '';
    miss_id_ent1 = ''; miss_id_ent2 = ''; miss_id_ent3 = ''; miss_id_ent4 = ''; miss_id_ent5 = '';
    misssel1 = '' ; misssel2 = ''; misssel3 = ''; misssel4 = '';misssel5 = ''
    outln1 = ''; outln2 = ''; outln3 = ''; outln4 = ''; outln5 = '';
    outl_id_ent1 = ''; outl_id_ent2 = ''; outl_id_ent3 = ''; outl_id_ent4 = ''; outl_id_ent5 = '';
    outlsel1 = '' ; outlsel2 = ''; outlsel3 = ''; outlsel4 = '';outlsel5 = ''
    othern1 = ''; othern2 = ''; othern3 = ''; othern4 = ''; othern5 = '';
    other_id_ent1 = ''; other_id_ent2 = ''; other_id_ent3 = ''; other_id_ent4 = ''; other_id_ent5 = '';
    othersel1 = '' ; othersel2 = ''; othersel3 = ''; othersel4 = '';othersel5 = ''
    boundn1 = ''; boundn2 = ''; boundn3 = ''; boundn4 = ''; boundn5 = '';
    bound_id_ent1 = ''; bound_id_ent2 = ''; bound_id_ent3 = ''; bound_id_ent4 = ''; bound_id_ent5 = '';
    boundsel1 = '' ; boundsel2 = ''; boundsel3 = ''; boundsel4 = '';boundsel5 = ''
    boundn1 = ''; boundn2 = ''; boundn3 = ''; boundn4 = ''; boundn5 = '';
    tabu_id_ent1 = ''; tabu_id_ent2 = ''; tabu_id_ent3 = ''; tabu_id_ent4 = ''; tabu_id_ent5 = '';
    tabusel1 = '' ; tabusel2 = ''; tabusel3 = ''; tabusel4 = '';tabusel5 = ''
    keep_ent1 = ''; keepsel1 = ''; keep_ent2 = ''; keepsel2 = ''; keep_ent3 = ''; keepsel3 = '';
    keep_ent4 = ''; keepsel4 = ''; keep_ent5 = ''; keepsel5 = ''; id_ent1 =''; id_ent2='';
    id_ent3='';id_ent4='';id_ent5='' ; checks_fame = '' ; erdlabel= '';
    session_type= ''; session_folder= '' ; session_file= ''; session_version = '';
    check_raw1_ent =''; check_raw2_ent='';check_raw3_ent=''; check_raw4_ent='';check_raw5_ent=''
    sel_frame = ''; abort =0; a_links = ''; attach_folder='' ; scto_user=''; scto_pass = ''; pb='';
    value_label=''; server_conn = 0 ; action_label = ''; curr_att =0

gloSettings()

# #################################
# Define variables for Restoration
# ##################################

# create a variable that keeps track of all variables in the settings
all_variable_names = []
for keys, values in list(globals().items()):
   if '__' not in keys and keys != 'gloSettings' and keys!= 'all_variable_names':
       all_variable_names.append(keys)


all_var_names_norm = ["parent_folder", "folder_name","num_raw_files","num_data_files",
                      "check_raw1", "check_raw2", "check_raw3","check_raw4", "check_raw5",
                      "check_raw1_ent", "check_raw2_ent", "check_raw3_ent", "check_raw4_ent", "check_raw5_ent",
                      "check_rawdata1", "check_rawdata2", "check_rawdata3", "check_rawdata4", "check_rawdata5"]

# Entry and combo-box variables
all_var_names_get = []
for i in range(1,6):
    all_var_names_get.append(f'r_run{i}')
    all_var_names_get.append(f'r_dup{i}')
    all_var_names_get.append(f'r_miss{i}')
    all_var_names_get.append(f'r_outl{i}')
    all_var_names_get.append(f'r_other{i}')
    all_var_names_get.append(f'r_bound{i}')
    all_var_names_get.append(f'r_tabu{i}')
    all_var_names_get.append(f'keep_ent{i}')
    all_var_names_get.append(f'id_ent{i}')
    all_var_names_get.append(f'check_raw{i}_ent')
    all_var_names_get.append(f'dup_id_ent{i}')


# Text variables
all_var_names_gett = []
for i in range(1, 6):
    all_var_names_gett.append(f'miss_id_ent{i}')
    all_var_names_gett.append(f'outl_id_ent{i}')
    all_var_names_gett.append(f'other_id_ent{i}')
    all_var_names_gett.append(f'bound_id_ent{i}')
    all_var_names_gett.append(f'tabu_id_ent{i}')


print(all_var_names_gett)
print(all_var_names_get)
