# File: 02 Train test split linux output chart.py
# Date: 06/05/2025

# Load required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
# Seaborn libraries
import seaborn as sns
sns.set_theme(style = "darkgrid")

# 1. Build function to split data into trian test sets

# Check data folder content
wd = os.getcwd()
print('My working directory is:',wd)

# 1.1 Change current WD to top folder directory to access \data sub-folder to load .csv data into python
project_directory = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python')
my_directory = os.chdir(project_directory)
wd = os.getcwd()
print('My new WD is:',wd)
