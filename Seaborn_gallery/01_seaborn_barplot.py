# File: 01_seaborn_barplot.py

# 1. Load basic libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

my_wd = os.getcwd()
print("My working directory is:",my_wd)



# 1. List files in \data folder to identify Excel file to be imported into Python 
new_wd_ML_using_python = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python")

# 2.change existing working directory to ML-using-Python folder to access Excel file located in \data folder
os.chdir(new_wd_ML_using_python)

new_wd = os.getcwd()
print("Changed working directory to:",new_wd)


# 3. Build path to Exel file to be imported from \data sub-folder
data_folder = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python",
                           'data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

# 3.1 Build  path to Excel file location
ine_population_nationality = os.path.join('data','INE total and foreign population figures Spain.xlsx')
print('ÍNE_population_nationality:',ine_population_nationality)

# 4. Import Excel into Python

# 4.1 Get tab names to choose which ones to import
import openpyxl

my_excel_file = pd.ExcelFile(ine_population_nationality)

my_excel_file.sheet_names  # see all sheet names

# 4.2 Imoprt Excel file into Python using pd.read_excel() method
INEdata = pd.read_excel(ine_population_nationality,
                                  sheet_name = 'INE_Total_foreign_population',
                                  skiprows= 2
                                )
INEdata.head()

INEdata.columns # Get column names from Pandas DataFrame imported Excel file

# Rename columns
INEdata.columns = ['Date','Total_population','Foreign_population','Percent_foreign_population',
'Total population YoY(N)','Total population  YoY(%)','Foreign population YoY(N)','Foreign population  YoY(%)']

# 5. Data wrangling

# 5.1 Subset columns from initial DataFrame

INE_total_foreign_population = INEdata[['Date','Total_population','Foreign_population']]
INE_total_foreign_population.head()

INE_total_foreign_population.head()

INE_total_foreign_population.info() # Get Pandas DataFrame data type columns info


# 5.2 Extract year from character Date column Pandas DataFrame  
# Using String slicing we will start creating new date variables from initial Srting Date column
# Using str[] parameter from str.strip() to slice four latest characters from Date column to obtain full year in YYYY format
# Retrieve character 13 to the end (to inlcude just Year part of the date)

INE_total_foreign_population['Year']  = INE_total_foreign_population['Date'].str.strip().str[13:]
INE_total_foreign_population.head()

INE_total_foreign_population.head()
