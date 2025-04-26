# File: 01 Train test split linux.py
# Date: 26/04/2025

# Load required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import math

# 1. Build function to split data into train and test sets 

# This is an adhoc function to split initial input data frame into Train and Test sets.
# The function has two parameters:
# - The data set you want to split defined by the "Inputdata" object
# - The percentage you want to assign to the Train split (usually 80%)

# 1.1 Check data folder content
wd = os.getcwd()
print('My working directory is:',wd)

# 1.1 Check top project folder path
project_directory = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python')
my_directory = os.chdir(project_directory)
wd = os.getcwd()
print('My new wd is',wd)
