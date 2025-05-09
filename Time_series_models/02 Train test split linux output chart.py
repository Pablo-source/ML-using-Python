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

# 1.2 Check files in \data sub-folder
data_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python','data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents are:',data_folder_contents)

# 1.3 Check .csv files available in the /data sub-folder
# I want to import .csv file "data/AE_Attendances_Aug2010_Mar_2025.csv"
for files in os.listdir(data_folder):
    if files.endswith('.csv'):
        print(files)
    else:
        continue

# 1.4 Import .csv file "AE_Attendances_Aug2010_Mar_2025.csv"
Attendances_file = os.path.join('data','AE_Attendances_Aug2010_Mar_2025.csv')

AE_data = pd.read_csv(Attendances_file,
                      parse_dates=['Period'])

AE_data.info()
AE_data.head()
# 2. Split initial Set into TypeI, TypeII, TypeII with Period column datasets
# To apply later the adhoc trainsplit() function created in previous script:

AE_data_TypeIATT = [['Period','Type1_ATT']]
AE_data_TypeIIATT = [['Period','Type2_ATT']]
AE_data_TypeIIIATT = [['Period','Type3_ATT']]