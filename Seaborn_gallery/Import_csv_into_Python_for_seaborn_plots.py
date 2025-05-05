# Fle: import_csv_into_Python_for_seaborn_plots.py
# Based on Jupyter notebook: Import_csv_into_Python_for_seaborn_plots.ipynb

# 1. Import required libraries 
import pandas as pd
import os

# Load specific seaborn libraries 
import seaborn as sns
import matplotlib.pyplot as plt 
sns.set_theme(style="darkgrid")

# 2. Built path to project folder
my_wd = os.getcwd()
print("My working directory is:", my_wd)

