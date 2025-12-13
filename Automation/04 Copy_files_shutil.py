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