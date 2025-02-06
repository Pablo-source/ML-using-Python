# File based on: "02_matplotlib_line_charts.qmd" file
# File: 01_matplotlib_line_charts.py

# 1. Load required modules
import pandas as pd
import numpy as np
import os

# 2. Import .csv data into Python.
wd = os.getcwd()
print(wd)

project_directory = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python")
my_direcory = os.chdir(project_directory)
wd = os.getcwd()
print(wd)

# data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
data_folder = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python","data")
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

print(data_folder)

# AE_Attendances_file = r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\AE_Attendances_2010_2024.csv'
# Load file using os.path.join() method
AE_Attendances_file = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python","data","AE_Attendances_2010_2024.csv")
print('path_to_Attendances_file:',AE_Attendances_file)

# Load data
AE_data = pd.read_csv(AE_Attendances_file,parse_dates=[0],date_format = '%d/%m/%Y')  
AE_data.head()

# Create new charts, first rename existing column names from imported .csv file
AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']
AE_data.columns
AE_data.head()

AE_data.info()
type(AE_data)

# 3. Line chart in matplotlib

## 3.1 Attendances TypeI line chart 
import matplotlib.pyplot as plt

AE_data.head()

# Create a matplotlib line chart 
plt.title("Attendances Type I in England. 2010-2024 Period.")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Type I Attendances 2010 2024 period.png', bbox_inches = 'tight')
plt.show()

## 3.2 Attendances TypeI, TypeII, TypeIII lines chart and save it as .png file under Plots folder
plt.title("Attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.plot(AE_data.Date,AE_data.Att_type2)
plt.plot(AE_data.Date,AE_data.Att_type3)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Matplotlib_gallery/Plots/Type I, II and III attendances 2010 2024 period_line_plot.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()
