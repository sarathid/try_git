# List of CNS Commands need to be found.
# Add the commands in list,if any missed.
CNS_VCL_COMMANDS =[
'ACTIVE_ALT SHUTOFF',
'ACTIVE_ALT STATUS',
'ACTIVE_ALT STATUS',
'ACTIVE_ALT VALUE',
'ACTIVE_REF SHUTOFF',
'ACTIVE_REF VALUE',
'AFCS_VERT ALT_CAPTURE',
'AFCS_VERT ALT_CHT_STATUS',
'AFCS_VERT ALT_HOLD',
'AFCS_VERT ALT_TRACK',
'AFCS_VERT FLT_LVL_CHNG',
'AFCS_VERT FLT_LVL_CHNG_STATUS',
'AFCS_VERT GS_AC_STATUS',
'AFCS_VERT GS_ARM',
'AFCS_VERT OVER_SPEED_STAT',
'AFCS_VERT OVERSPEED',
'AFCS_VERT PITCH_MODE',
'AFCS_VERT PITCH_MODE_STAT',
'AFCS_VERT SHUTOFF',
'AFCS_VERT VERT_SPD_HOLD',
'AFCS_VERT VERT_SPD_HOLD_STAT',
'AFCS_VERT VERT_TAKEOFF',
'AFCS_VERT VERT_TAKEOFF_STAT',
'AFCS_VERT VNAV_ALT_ABORT',
'AFCS_VERT VNAV_ALT_ABORT_STAT',
'AFCS_VERT VNAV_GP_AC_STATUS',
'AFCS_VERT VNAV_GP_ARM',
'AFCS_VERT VNAV_GP_CAP',
'AFCS_VERT VNAV_PATH_CAP',
'AFCS_VERT VNAV_PATH_CAP_STAT',
'AFCS_VNAV_MODE ARM',
'AFCS_VNAV_MODE SHUTOFF',
'AFCS_VNAV_MODE STATUS',
'AFCS_VNAV_MODE WARN',
'AP_ENGAGE AP_ENGAGED',
'AP_ENGAGE AP_ENGAGED_STATUS',
'AP_ENGAGE PITCH_OUTER_STATUS',
'AP_ENGAGE PITCH_OUTER_VALID',
'AP_ENGAGE SHUTOFF',
'APPR_STR_ARM VALUE',
'APPR_STR_ARM SHUTOFF',
'APPR_STR_ARM STATUS',
'APPR_STR_CAP VALUE',
'APPR_STR_CAP SHUTOFF',
'APPR_STR_CAP STATUS',
'BARO_CORRECTED_ALT SHUTOFF',
'BARO_CORRECTED_ALT STATUS',
'BARO_CORRECTED_ALT VALUE',
'CNS_SIM SHUTOFF',
'COMP_VER_VEL SHUTOFF',
'COMP_VER_VEL STATUS',
'COMP_VER_VEL VALUE',
'EGYPTIAN_C130 TEST_OFF',
'EGYPTIAN_C130 TEST_ON',
'ENGINE_RUNNING LEFT',
'ENGINE_RUNNING RIGHT',
'ENGINE_RUNNING SHUTOFF',
'ENGINE_RUNNING STATUS',
'EXT_NAV_COMMAND SET_EXT_NAV_COMM',
'EXT_NAV_COMMAND SET_EXT_NAV_COMM_STATUS',
'EXT_NAV_COMMAND SHUTOFF',
'FMS_SPD_ON IAS_BIAS',
'FMS_SPD_ON USE_VALUE',
'FUEL_FLOW SHUTOFF',
'FUEL_FLOW STATUS',
'FUEL_FLOW VALUE',
'HALF_BANK_SEL SHUTOFF',
'HALF_BANK_SEL STATUS',
'HALF_BANK_SEL VALUE',
'IAS_REF SEL_REF',
'IAS_REF SEL_REF_STATUS',
'IAS_REF SHUTOFF',
'IAS_REF SOURCE',
'IAS_REF SOURCE_STATUS',
'INDICATED_AIR SHUTOFF',
'INDICATED_AIR STATUS',
'INDICATED_AIR VALUE',
'LAT_GO_AROUND SHUTOFF',
'LAT_GO_AROUND STATUS',
'LAT_GO_AROUND VALUE',
'MACH_REF SEL_REF_STATUS',
'MACH_REF SOURCE',
'MACH_REF SOURCE_STATUS',
'MACH_REF SEL_REF',
'MACH_REF SHUTOFF',
'MAX_OP_MACH SHUTOFF',
'MAX_OP_MACH STATUS',
'MAX_OP_MACH VALUE',
'MAX_OP_SPEED SHUTOFF',
'MAX_OP_SPEED STATUS',
'MAX_OP_SPEED VALUE',
'NAV_ARM SHUTOFF',
'NAV_ARM STATUS',
'NAV_ARM VALUE',
'NAV_CAP SHUTOFF',
'NAV_CAP STATUS',
'NAV_CAP VALUE',
'NAV_SOLN ACTUAL_NAV_PERF_STATUS',
'NAV_SOLN ACTUAL_NAV_PERF_VALUE',
'NAV_SOLN DRIFT_ANGLE_STATUS',
'NAV_SOLN DRIFT_ANGLE_VALUE',
'NAV_SOLN EST_POS_UNCERT_STATUS',
'NAV_SOLN EST_POS_UNCERT_VALUE',
'NAV_SOLN GPS_HIL_STATUS',
'NAV_SOLN GPS_HIL_VALUE',
'NAV_SOLN GPS_IN_NAV_SOLN',
'NAV_SOLN GROUND_SPEED',
'NAV_SOLN GROUND_SPEED_STATUS',
'NAV_SOLN MAG_HEADING_STATUS',
'NAV_SOLN MAG_HEADING_VALUE',
'NAV_SOLN MAG_VARIATION_STATUS',
'NAV_SOLN MAG_VARIATION_VALUE',
'NAV_SOLN MOD_LAT',
'NAV_SOLN MOD_LON',
'NAV_SOLN MOD_UTC',
'NAV_SOLN NAV_DATA_STATUS',
'NAV_SOLN NAV_MODE',
'NAV_SOLN SET_LAT',
'NAV_SOLN SET_LON',
'NAV_SOLN SET_UTC',
'NAV_SOLN SHUTOFF',
'NAV_SOLN TRACK_ANGLE_STATUS',
'NAV_SOLN TRACK_ANGLE_VALUE',
'NAV_SOLN TRUE_HEADING_STATUS',
'NAV_SOLN TRUE_HEADING_VALUE',
'NAV_SOLN WIND_COMPUTED',
'NAV_SOLN WIND_DIRECTION',
'NAV_SOLN WIND_SPEED',
'NAV_SOLN WIND_STATUS',
'NAV_SOURCE SET_ACT_NAV_SRC',
'NAV_SOURCE SET_ACT_NAV_STATUS',
'NAV_SOURCE SHUTOFF',
'PERSONALITY_FILE_READ',
'PERSONALITY_FILE_READ USE_PATH',
'PRESELECT_ALT KNOB',
'PRESELECT_ALT STATUS',
'PRESELECT_ALT VALUE',
'PRESELECT_SRC SHUTOFF',
'PRESELECT_SRC STATUS',
'PRESELECT_SRC VALUE',
'PRESSURE_ALT SHUTOFF',
'PRESSURE_ALT STATUS',
'PRESSURE_ALT VALUE',
'STATIC_AIR_TEMP SHUTOFF',
'STATIC_AIR_TEMP STATUS',
'STATIC_AIR_TEMP VALUE',
'TOTAL_FUEL_QUANTITY SHUTOFF',
'TOTAL_FUEL_QUANTITY STATUS',
'TOTAL_FUEL_QUANTITY VALUE',
'TRANSFER_AUTOPILOT SHUTOFF',
'TRANSFER_AUTOPILOT STATUS',
'TRANSFER_AUTOPILOT VALUE',
'TRUE_AIR SHUTOFF',
'TRUE_AIR STATUS',
'TRUE_AIR VALUE',
'VERT_GO_AROUND SHUTOFF',
'VERT_GO_AROUND STATUS',
'VERT_GO_AROUND VALUE',
'VERT_VEL SHUTOFF',
'VERT_VEL STATUS',
'VERT_VEL VALUE',
'WOW SHUTOFF',
'WOW STATUS',
'WOW VALUE']

import re
import os
all_files=[]
Command_result={}
file_result={}
filelocation=raw_input("Enter test Directory path:")
if (os.path.isdir(filelocation)== False):
    print "Path entered is invalid..Try again.."
else:
    output_path=raw_input("Enter output path :")
    if (os.path.isdir(output_path)== False):
        print "Path entered is invalid."
        print "I'm going to place report in "
        print filelocation
        output_path=filelocation
    for command in CNS_VCL_COMMANDS:
            Command_result[command]=[]
    for dirpath,dir_names,file_names in os.walk(filelocation):
        for file_name in file_names:
            all_files.append(dirpath+'\\'+file_name)
    for file_path in all_files:
        filepath,filename=os.path.split(file_path)
        if(filename[-3:]=='vcl'):
            print "Searching in file : "+filename
            for command in CNS_VCL_COMMANDS:
                file_Content = open(file_path).read()
                splited_command=command.split(' ')
                if(len(splited_command)>=2):
                    search_pattern = splited_command[0]+'\s*'+splited_command[1]
                else:
                    search_pattern = command
                if(len(re.findall(search_pattern,file_Content,re.I)) > 0):
                    print re.findall(search_pattern,file_Content,re.I)
                    if filename not in Command_result[command]:
                        Command_result[command].append(filename)
                    if filename not in file_result.keys():
                        file_result[filename]=[command]
                    else:
                        file_result[filename].append(command)
    # Creating Report file for CNS Commands.
    # Creating Report Commands present in Files.
    Command_Report=open(output_path+'\\CommandReport.csv','w')
    Command_Report.write('Command,'+'File name'+'\n')
    for command in Command_result.keys():
        for filename in Command_result[command]:
            Command_Report.write(command+','+filename+'\n')
    Command_Report.close()
    # Creating report file for CNS Commands.
    #Creating report Files corresponding commands present.
    File_Report=open(output_path+'\\File_Report.csv','w')
    File_Report.write('Filename,'+'Command'+'\n')
    for filename in file_result.keys():
        for command in file_result[filename]:
            File_Report.write(filename+','+command+'\n')
    File_Report.close()
print '*'*80
print "Search completed in "+str(len(all_files))+' files.'
print str(len(file_result.keys()))+" files are having External Nav commands."
print '*'*80    
print "CommandReport.csv and FileReport.csv are generated in "
print output_path
raw_input()