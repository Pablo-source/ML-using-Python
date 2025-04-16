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
#  C:\Repos\ML-using-Python
 
AE_Attendances_file = r'C:\Repos\ML-using-Python\data\AE_Attendances_2010_2024.csv'

project_directory_main = r'C:\Repos\ML-using-Python'
my_direcory = os.chdir(project_directory_main)
wd = os.getcwd()
print(wd)

os.chdir('C:/Pablo UK/46 DATA SCIENCE all/10 ML python JULY 2021')
# Read in dataset