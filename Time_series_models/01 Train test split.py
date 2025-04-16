# File: 01 Train test split.py
# Date: 14/04/2025

# 1. Load required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import math

# ### 1. Split initial data into Train and Test sets
# We have designed a function to split initial input data frame into Train and Test sets.
# The function has two parameters:
# - The data set you want to split defined by the "Inputdata" object
# - The percentage you want to assign to the Train split (usually 80%)

# 1. Check data folder content
wd = os.getcwd()
print('My working directory is:',wd)

# My working directory is: c:\Repos\ML-using-Python\data_wrangling_scripts
#  c:\Repos\ML-using-Python\Time_series_models
 
project_directory_main = os.path.join('c:/','Repos','ML-using-Python')
my_direcory = os.chdir(project_directory_main)
wd = os.getcwd()
print(wd)

# Chedk files in our \data sub-folder
data_folder = os.path.join('c:/','Repos','ML-using-Python','data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)


# 2. Build path to this "AE_Attendances_2010_2024.csv" file we want to import into Python



# Read in dataset