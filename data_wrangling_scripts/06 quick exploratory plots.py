# 06 Quick exploratory plots.py
# AIM: This is a way of quickly explore some columns from a newly loaded Pandas DataFrame

import pandas as pd
import os

# 1. Check data folder content
wd = os.getcwd()
print('My working directory is:',wd)

project_directory = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python")
my_direcory = os.chdir(project_directory)
wd = os.getcwd()
print(wd)

# 2. Cheeck dat folder contents using os.path.join() function
data_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python','data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

# 3. Load 'AE_Attendances_2010_2024.csv' file using os.walk
# Inside /data folder: /home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/data
# .csv file to import: /home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/data/AE_Attendances_2010_2024.csv

attendances_file = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python","data","AE_Attendances_2010_2024.csv")
print(attendances_file)

# 4. Load Attendances data using Pandas read_csv() function
AE_data = pd.read_csv(attendances_file,parse_dates=[0],date_format = '%d/%m/%Y')  
AE_data.head()

print(attendances_file)


AE_data_new = pd.read_csv(attendances_file,parse_dates=[0], date_format='%d/%m/%Y')
AE_data_new.info()
AE_data_new.head()