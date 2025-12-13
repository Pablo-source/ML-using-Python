# File: 04 Copy_files_shutil.py

import os
from os import path
import glob
import shutil

print(f"Script to practise how to copy files using functions")

# Current WD
wd = os.getcwd()
print(wd)
print(f'working on the cloned folder:{wd}')

# Project directories
folders_list = os.listdir()
print(f'Current folder structure:{folders_list}')

# Create two new folders to Copy files: 
# "Test_folder_A" and "Test_folder_B"
def create_new_folders():
    if not path.exists("Test_folder_A"):
        os.mkdir("Test_folder_A")
    if not path.exists("Test_folder_B"):
        os.mkdir("Test_folder_B")
    print("Created Test A and Test B origin destination folders!")
# Execute function
create_new_folders()

# 1. List files on "Test_folder_A" to be moved to "Test_folder_B"
# Check .csv files available in the /data sub-folder
# I want to import .csv file "data/AE_Attendances_Aug2010_Mar_2025.csv"

# data_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python','data')

Test_folder_A = os.path.join('C:','Users','pituf','OneDrive','Documentos','Pablo','DELL_python_github','ML-using-Python','Test_folder_A')
Test_folder_A_contents = os.listdir(Test_folder_A)

# for files in os.listdir(data_folder):
#    if files.endswith('.csv'):
#         print(files)
#    else:
#        continue