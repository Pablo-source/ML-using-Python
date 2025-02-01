# File: 05 Setup relative paths os path join.py
# AIM: using os.path.join() method to load data using relative paths

import pandas as pd
import os

wd = os.getcwd()
print(wd)

data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/data'
print(data_folder)


# 1. Previous way of loading data using r'/ and hardcoded paths

# 1.1 List files on my data folder

data_folder_files = os.listdir(data_folder)
print(data_folder_files)

## ['wine_quality.zip', 'winequality.names', 'Monthly-AE-Time-Series-January-2024.xls', 'AE_Time_Series_Data_website.txt', 'winequality-red.csv', 'OCDE_countries_population_figures_1970_2022.csv', 'all_wine_reset.csv', 'AE_Attendances_2010_2024.csv', 'ONS_Figure_2__Population_increase_in_mid-2023_was_driven_mostly_by_net_international_migration.xls', 'winequality-white.csv', 'monthly-milk-production-pounds.csv', 'ONS_Figure_01_Long_term_emigration_immigration_net_migration.xlsx', 'ONS_long_term_immigration_end2024.xlsx']

# 1.1 Load  AE_Attendances_2010_2024.csv file from previous /data folder 
# This first time NOT using os.path.join() method
# 'AE_Attendances_2010_2024.csv',

AE_Attendances_file = r'/home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/data/AE_Attendances_2010_2024.csv'
print(AE_Attendances_file)

# 1.2 load AE Attendances data using pandas read_csv() function
# Parse dates to import date format into Python from CSV

AE_data = pd.read_csv(AE_Attendances_file, parse_dates=[0],
                      date_format='%d/%m/%Y')
AE_data.head()

# Get AE_data data frame properties
AE_data.info()   # Period column correctly imported as date variable: datetime64[ns]
AE_data.dtypes
AE_data.columns

# 2. Using os.path.join() function
# This is a better way to imoprt dat into Python using relative paths in python provided by os.path.join() function

data_folder = os.path.join("/home","pablo","Documents","Pablo_zorin","VS_Python_GitHub_Pablo_source/ML-using-Python","data")
print(data_folder) 
# List files now from path defined by os.path.join() method
data_folder_files = os.listdir(data_folder)
print(data_folder_files)
