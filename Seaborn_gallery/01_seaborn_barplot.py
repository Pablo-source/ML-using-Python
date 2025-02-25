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
