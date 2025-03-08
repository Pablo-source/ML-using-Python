# File: 02_percent_barplot_population_nationality.py
# Date: 08/03/2025

# This notebook will contain examples of stakced and percent barplots created using Seaborn. 
# Plots data used will be INE (Spanish National Institute) Spanish Office of National statistics
#  demographic time series indicators such as total population and population by nationality as 
# of 1st January and also by foreign population by country of birth.

# Load required libraries
import pandas as pd
import os



# 1. Build path to project folder

# Get current working directory
my_wd = os.getcwd()
print("My working directory is:",my_wd)

# 1. List files in \data folder to identify Excel file to be imported into Python 
new_wd_ML_using_python = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python")

# 2.change existing working directory to ML-using-Python folder to access Excel file located in \data folder
os.chdir(new_wd_ML_using_python)

new_wd = os.getcwd()
print("Changed working directory to:",new_wd)


# 2. Build path to Exel file to be imported from \data sub-folder

# - First we check the contents in our data folder to find Excel file to import into Python

# 2.1. Build path to Exel file to be imported from \data sub-folder
data_folder = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source","ML-using-Python",
                           'data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

# 2.2 Build  path to Excel file location
ine_population_nationality = os.path.join('data','INE total and foreign population figures Spain.xlsx')
print('ÍNE_population_nationality:',ine_population_nationality)


# 3. Import Excel file into Python 
# Then we build path to Excel file we will load in Python using Pandas 
# Get individual tab names from previous "INE total and foreign population figures Spain.xlsx" file

my_excel_file = pd.ExcelFile(ine_population_nationality)

my_excel_file.sheet_names  # see all sheet names

INEdata = pd.read_excel(ine_population_nationality,
                                  sheet_name = 'INE_Total_foreign_population',
                                  skiprows= 2
                                )
INEdata.head()

#  Keep only first 20 rows to skip footnotes
INE_data_clean = INEdata.head(20)

#  Rename columns
INE_data_clean.columns = ['Date','Total_population','Foreign_population','Percent_foreign_population',
'Total population YoY(N)','Total population  YoY(%)','Foreign population YoY(N)','Foreign population  YoY(%)']

# 4. Create new calculated fields 
