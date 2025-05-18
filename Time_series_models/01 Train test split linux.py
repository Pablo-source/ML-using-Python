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

# Check data folder content
wd = os.getcwd()
print('My working directory is:',wd)

# 1.1 Check top project folder path
project_directory = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python')
my_directory = os.chdir(project_directory)
wd = os.getcwd()
print('My new wd is',wd)

# 1.2 check files in \data sub-folder to be onboarded into Pyhon
data_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python','data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

# 1.3 Check .csv files as I want to import just .csv files
for files in os.listdir(data_folder):
    if files.endswith('.csv'):
        print(files)
    else:
        continue

# 1.4 Import .csv file "AE_Attendances_2010_2025.csv"
Attendances_file = os.path.join('data','AE_Attendances_2010_2024.csv')

AE_data = pd.read_csv(Attendances_file,
                      parse_dates=True)
AE_data.head()
AE_data.tail()

# 1.4.1 Turn Period colum into date format in Python
# Convert Period column to date format pd.to_datetime(df['column])
AE_data['Period'] = pd.to_datetime(AE_data['Period'])
AE_data.head()


# 1.5 Create three dataset based on Type1_ATT, Type2_ATT and Type3_ATT

# 1.5.1 Creating dataset for Type1_ATT
AE_data.info()
AE_data_TypeI = AE_data[['Period','Type1_ATT']]
AE_data_TypeI.head()
AE_data_TypeI.tail()

AE_data_TypeI_min_date = AE_data_TypeI['Period'].min()
print('AE_data_TypeI_min_date',AE_data_TypeI_min_date)
AE_data_TypeI_max_date = AE_data_TypeI['Period'].max()
print('AE_data_TypeI_max_date',AE_data_TypeI_max_date)

# Output this AE_data_TypeI file as .csv including AE Type I and date columns
AE_data_TypeI.info()
AE_data_TypeI.to_csv('data/AE_Attendances_TypeI_2010_2025.csv')


# 1.6 Function to split input data into train and test sets
# Arguments: Function must include an argument to specify the TRAIN set as percentage of total rows.
# Outputs: Function must return two CSV files with Train set and test sets splits from original input file

def traintestsplit(Inputdata,perctrain):
    """Split main data set into train and test sets,
    where TRAIN percentage is defined by user"""

    train_calc = math.ceil(((len(Inputdata.index)*perctrain/100)))
    """"Now we use the total number of rows defined by train_calc to slice Input data,
    using .iloc method"""
    train = Inputdata.iloc[0:train_calc,] 
    """"Then turn this train set into a Dataframe and output it as .csv file"""
    train_output = pd.DataFrame(train)
    train_output.to_csv('data/Type_I_ATT_TRAIN.csv',index=False)
    """The remaining set of rows correspond to the TEST set, until end of rows of
    initial Input data"""
    test = Inputdata.iloc[train_calc:,]
    """"Then turn this test set into a Dataframe and output it as .csv file"""
    test_output = pd.DataFrame(test)
    test_output.to_csv('data/Type_I_ATT_TEST.csv',index=False)
    """Finally our function returns TWO DATAFRAMES train_output and test_output"""
    return train_output, test_output

## Now we can test the function with our previous AE_data_TypeI Dataframe
# The above function outputs two CSV files for Type I ATT initial data split
# One csv called "Type_I_ATT_TRAIN.csv" for TRAIN set and "Type_I_ATT_TEST.csv" for TEST set
traintestsplit(AE_data_TypeI, 80)
