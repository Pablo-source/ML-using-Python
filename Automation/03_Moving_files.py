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

# 1.1 Moving files from "Test_files_A" folder to "Test_files_B" folder