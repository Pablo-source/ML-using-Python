# File: Unzip data files relative paths.py
# How to unzip file "archive.zip"

# Load required libraries
import pandas as pd
import os
from zipfile import ZipFile

my_wd = os.getcwd()
print("My working directory is:",my_wd)

## I will need to change WD to the \Python Scripts top folder to acccees the \data sub folder
python_scripts_folder = os.path.join('C:/','Users','OGTSLCEF','OneDrive - NHS','Documents','Python Scripts')
print(python_scripts_folder)

# So I change current directory to this \Python Scripts higher level
os.chdir(python_scripts_folder)

new_wd = os.getcwd()
print("Changed working directory to:",new_wd)

# We provide first the path to the data folder:
data_folder = os.path.join('C:/','Users','OGTSLCEF','OneDrive - NHS','Documents','Python Scripts','data')
print('Data folder:',data_folder)

# Then we can scan that folder to retrive just files with .zip extension
for files in os.listdir(data_folder):
    if files.endswith('.zip'):
        print(files)
    else:
        continue

# Unzip that "archive.zip" file from data folder back into the samve \data folder
archive_zip_file =  os.path.join('C:/','Users','OGTSLCEF','OneDrive - NHS','Documents','Python Scripts','data','archive.zip')
# 1.2.1.2 But this time I provide a new path to the DESTINATION folder of the unzipped file: 
data_folder = os.path.join('C:/','Users','OGTSLCEF','OneDrive - NHS','Documents','Python Scripts','data')
# 1.2.2 Then I use withZipFile() providing this alternative location
# Using now Original file location and destination path folder.
with ZipFile(archive_zip_file,'r') as zObject:
    zObject.extractall(
        path = data_folder
    )

# Initial zipped file: archive.zip    
# Unzipped files: complete.csv, scrubbed.csv