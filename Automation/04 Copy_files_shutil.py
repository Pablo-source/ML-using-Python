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