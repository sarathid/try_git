# List of Commands need to be found.
# Add the commands in list,if any missed.
COMMANDS =[]

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
    for command in COMMANDS:
            Command_result[command]=[]
    for dirpath,dir_names,file_names in os.walk(filelocation):
        for file_name in file_names:
            all_files.append(dirpath+'\\'+file_name)
    for file_path in all_files:
        filepath,filename=os.path.split(file_path)
        if(filename[-3:]=='.py'):
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
print str(len(file_result.keys()))+" files are having commands."
print '*'*80    
print "CommandReport.csv and FileReport.csv are generated in "
print output_path
raw_input()
