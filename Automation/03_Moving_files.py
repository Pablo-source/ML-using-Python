# Script: 03_Moving_files.py

import os
from os import path
import glob
import shutil

print(f'Script to practise shutil moving files functions')


# Downloads = '/home/pablo/Downloads'

# Curr_dir = os.chdir(Downloads)
wd = os.getcwd()
print(wd)

# Change current directory to /ML-using-Python
ML_using_python_project = '/home/pablo/Documents/Pablo_ubuntu/Python_github_projects'
Curr_dir = os.chdir(ML_using_python_project)

wd = os.getcwd()
print(wd)
print(f'working on the cloned folder:{wd}')

# 1. Create new testing folder called "Test_files_A" and "Test_files_B"
# Inside existing /Python_github_projects fodler
def testing_folders_setup():
    if not path.exists("Test_files_A"):
        os.mkdir("Test_files_A")    
    if not path.exists("Test_files_B"):
        os.mkdir("Test_files_B")
    
    print("Created new testing folders")

testing_folders_setup()


## 1. Moving files using Shutil

# 1.1 Check current WD
ML_using_python_project = '/home/pablo/Documents/Pablo_ubuntu/Python_github_projects'
Curr_dir = os.chdir(ML_using_python_project)
wd = os.getcwd()

print(f"My Current Working Directory is{wd}")

# 1.2 Check files to move are present in /Test_files_A sub-folder
files_directories = os.listdir(wd)
print(f"Files and directories in wd:{files_directories}")

csv_files = glob.glob(r'Test_files_A/*.csv')
print(f"Existing csv files in Test_files_A sub_folder:{csv_files}")
print(len(csv_files))

#    for item in range(len(csv_files)):
#        print(csv_files[item])
    # Now we move each .csv file to the previously created 04 csv_files folder
#        original = csv_files[item]
#       target = r'ML-using-Python/Test_files_B'
#       shutil.move(original, target)
#       print(f"file{item},has been moved to 04 csv_files folder")

