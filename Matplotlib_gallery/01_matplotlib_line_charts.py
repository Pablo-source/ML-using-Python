# File based on: "02_matplotlib_line_charts.qmd" file
# File: 01_matplotlib_line_charts.py

# 1. Load required modules
import pandas as pd
import numpy as np
import os

# 2. Import .csv data into Python.
wd = os.getcwd()
print(wd)

data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
print(data_folder)

AE_Attendances_file = r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\AE_Attendances_2010_2024.csv'

AE_data = pd.read_csv(AE_Attendances_file,
parse_dates=[0],
                      date_format = '%d/%m/%Y')  

AE_data.head()

# Create new charts

AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']
AE_data.columns
AE_data.head()

AE_data.info()
type(AE_data)

# 3. Line chart in matplotlib

## 3.1 Attendances TypeI line chart 
import matplotlib.pyplot as plt

AE_data.head()

plt.title("Attendances Type I in England. 2010-2024 Period.")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Type I Attendances 2010 2024 period.png', bbox_inches = 'tight')
plt.show()

## 3.2 Attendances TypeI, TypeII, TypeIII lines chart 
plt.title("Attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.plot(AE_data.Date,AE_data.Att_type2)
plt.plot(AE_data.Date,AE_data.Att_type3)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Plots/Type I, II and IIII attendances 2010 2024 period_line_plot.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()
