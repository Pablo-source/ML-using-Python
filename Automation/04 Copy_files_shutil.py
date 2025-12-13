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

test_folder_A = r'C:\Users\pituf\OneDrive\Documentos\Pablo\DELL_python_github\ML-using-Python\Test_folder_A'
my_directory = os.chdir(test_folder_A)

wd = os.getcwd() 
print(wd)

for files in os.listdir(test_folder_A): 
    if files.endswith('.csv'):
         print(files)
    else:
        continue

# 2. List files on "Test_folder_B" destination folder:
test_folder_B = r'C:\Users\pituf\OneDrive\Documentos\Pablo\DELL_python_github\ML-using-Python\Test_folder_B'

for files in os.listdir(test_folder_B): 
    if files.endswith('.csv'):
         print(files)
    else:
        continue

# 3. Copy files from "Test_folder_A" to "Test_folder_B" destination folder:

csv_files = glob.glob(r'Test_folder_A/*.csv')
print(f"Existing csv files in Test_files_A sub_folder:{csv_files}")
print(len(csv_files))

# 1.2 Move files from Test_files_A folder to Test_files_B folder using Shutil module
for item in range(len(csv_files)):
    print(csv_files[item])
 # Now we move each .csv file to the previously created 04 csv_files folder
    original = csv_files[item]
    target = r'Test_folder_B'
    shutil.copy(original, target)
    print(f"file{item},has been moved to Test_files_B folder")