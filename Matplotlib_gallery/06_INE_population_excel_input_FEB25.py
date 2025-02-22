# File: 06_INE_population_excel_input_FEB25.py
# Input File:(Excel)

# 1. Load required libraries

import pandas as pd
import os


# 2.Import Excel file into Python 

my_wd = os.getcwd()
print("My working directory is:",my_wd)

# 2.1 List files in \data folder to identify Excel file to be imported into Python 
new_wd_ML_using_python = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python")

# And we change existing working directory to this new folder
os.chdir(new_wd_ML_using_python)

new_wd = os.getcwd()
print("Changed working directory to:",new_wd)

data_folder = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python",
                           'data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

# 2.2 Build  path to Excel file location
ine_population_nationality = os.path.join('data','INE total and foreign population figures Spain.xlsx')
print('ÍNE_population_nationality:',ine_population_nationality)

# 2.2 Importing Excel file into python Section

import openpyxl

# 2.2.1 First we display sheet names from the Excel file we want to import into Python. We want to identify the speicific tab to be imported into Python 

xl = pd.ExcelFile(ine_population_nationality)

xl.sheet_names  # see all sheet names

#xl.parse(sheet_name)  # read a specific sheet to DataFrame

# 2.2.2 Import Excel file into python using Pandas read_excel() method

INEdata_input_test = pd.read_excel(ine_population_nationality)
INEdata_input_test.head()

# 2.2.3 We want to import data from Specifit Excel tab name
# Importing data into Python from "INE_Total_foreign_population" Excel file tab
ine_population_nationality = os.path.join('data','INE total and foreign population figures Spain.xlsx')

INEdata_third_tab = pd.read_excel(ine_population_nationality,
                                  sheet_name='INE_Total_foreign_population')
INEdata_third_tab.head()

# Then we want to be skip first row of data from third tab, as it contains null values that we want to ommit from our initial Excel data ingestion into Python.
INEdata_skip_rows = pd.read_excel(ine_population_nationality,
                                  sheet_name = 'INE_Total_foreign_population',
                                  skiprows= 2
                                )
INEdata_skip_rows.head()

INEdata_skip_rows.columns

# Now that we have original columns names imported into Python
INE_data = INEdata_skip_rows.copy()
INE_data.head()

# Rename columns
INE_data.columns = ['Date','Total_population','Foreign_population','Percent_foreign_population',
'Total population YoY(N)','Total population  YoY(%)','Foreign population YoY(N)','Foreign population  YoY(%)']


# 3.Re-create calculated fields 
# Recreate existing calculated fields "Percent_foreign_population" and "Total population YoY(N)" from
# #  initial "Total_Population" and "Foreign_population" columns:

# 3.1 - Then we introduce the first new calculated field "Percent_foreign_population" it is just a Foreign_population / Total_population
INE_calc = INE_data[['Date','Total_population','Foreign_population']]
INE_calc.head()

INE_calc['Percent_foreign_population'] = INE_calc['Foreign_population']/INE_calc['Total_population']
INE_calc.head()

# And we express calculation as percentage 
INE_calc['Percent_foreign_population'] = (INE_calc['Foreign_population']/INE_calc['Total_population']) *100
INE_calc.head()

# 3.2 Round previous calculated filed "Percent_foreign_population" using a lambda function
# Using a lambda() function lambda x:round(x,2) with the .apply() method
INE_calc['Percent_foreign_rounded'] = INE_calc['Percent_foreign_population'].apply(lambda x:round(x,2))
INE_calc.head()

# Subset just columns including latest calculations from origninal dataframe
INE_first_calc = INE_calc[['Date','Total_population','Foreign_population','Percent_foreign_rounded']]
INE_first_calc.head()