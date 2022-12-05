##hg
#check modified date and create the path if not exist

import os
import datetime as dt
import glob
import shutil

# Set folder or ask for user input
download = r'C:\Users\Henry.Gu\Downloads'
if 'download' in locals():
    print(download)
else:
    download = input(r'Enter folder') # ask user for Path

os.chdir(download)

# -- List files
#filenames = next(os.walk(download))
#os.listdir()
#glob.glob("*") 
list_of_ext = ('sql')
list_of_files = glob.glob("*") 

def clean_downloadsfolder_2():
    os.chdir(download)
    for file in list_of_files:
        if file.endswith(list_of_ext):
            if os.path.isfile(file):
                file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
                print(file)
                print(file_time.strftime("%Y-%m-%d"))
                filename, file_ext = os.path.splitext(file)
                file_ext_name = file_ext.replace(".","")
                print(filename,file_ext,file_ext_name)
                if not os.path.exists(str(file_time.strftime("%Y-%m-%d"))):
                    os.mkdir(str(file_time.strftime("%Y-%m-%d")))
                    if not os.path.exists(str(file_time.strftime("%Y-%m-%d"))+'/'+file_ext_name):
                        os.mkdir(str(file_time.strftime("%Y-%m-%d"))+'/'+file_ext_name)
                shutil.move(file, str(file_time.strftime("%Y-%m-%d"))+'/'+file_ext_name)