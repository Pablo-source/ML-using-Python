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