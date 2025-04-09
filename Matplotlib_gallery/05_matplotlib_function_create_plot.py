# Date:11/02/2025
# Script: 05_matplotlib_function_create_plot.py
# AIM: Create Matplotlib line chart and save it using a function

# Import required libraries
import pandas as pd
import os
from os import path

# 1.Check data folder files content
wd = os.getcwd()
print(wd)

data_folder = r"c:\Users\pituf\OneDrive\Documentos\Pablo\DELL_PYTHON_projects\data"
data_folder_files = os.listdir(data_folder)
print('data folder contents:',data_folder_files)

GDP_folder = r"c:\Users\pituf\OneDrive\Documentos\Pablo\DELL_PYTHON_projects\data\abmi_Gross_Domestic_Product"
GDP_folder_files = os.listdir(GDP_folder)
print('GDP_folder_contents:',GDP_folder_files)

wd = os.getcwd()
print(wd)

## 2. Load AE_data to create plots using Matplotlib

# Define path to 
AE_data_file = r"c:\Users\pituf\OneDrive\Documentos\Pablo\DELL_PYTHON_projects\data\AE_Attendances_2010_2024.csv"
print(AE_data_file)

# Load data
AE_data = pd.read_csv(AE_data_file,parse_dates=[0],date_format = '%d/%m/%Y')  
AE_data.head()

AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']
AE_data.columns
AE_data.head()

## 3. Create a plot for Type I Attendances data

import matplotlib.pyplot as plt

plt.title("Attendances Type I in England. 2010-2024 Period.")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Type I Attendances 2010 2024 period.png', bbox_inches = 'tight')
plt.show()

# 4. Function to create new "plots" folder
## This is an adhoc function to create folders in Python
def project_setup(file_name):
    """Create new folder"""
    if not path.exists(file_name):
        os.mkdir(file_name)

project_setup(file_name = "Plots")

# 5. Save plot in newly created "plots" folder
# Plot Att_type1
plt.title("Attendances Type I in England. 2010-2024 Period.")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Plots/Type I Attendances 2010 2024 period.png', bbox_inches = 'tight')
plt.show()

# Plot Att_type2
plt.title("Attendances Type II in England. 2010-2024 Period.")
plt.plot(AE_data.Date,AE_data.Att_type2)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Plots/Type II Attendances 2010 2024 period.png', bbox_inches = 'tight')
plt.show()

# 6. wip (create new plots using new function to create plots including a single 
# parameter to chooose which metric to create the plot for.
# The output plot must be saved in the \Plots sub-folder