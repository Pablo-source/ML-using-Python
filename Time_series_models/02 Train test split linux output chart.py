# File: 02 Train test split linux output chart.py
# Date: 06/05/2025

# Load required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
# Seaborn libraries
import seaborn as sns
sns.set_theme(style = "darkgrid")

# 1. Build function to split data into trian test sets

# Check data folder content
wd = os.getcwd()
print('My working directory is:',wd)

# 1.1 Change current WD to top folder directory to access \data sub-folder to load .csv data into python
project_directory = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python')
my_directory = os.chdir(project_directory)
wd = os.getcwd()
print('My new WD is:',wd)

# 1.2 Check files in \data sub-folder
data_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python','data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents are:',data_folder_contents)

# 1.3 Check .csv files available in the /data sub-folder
# I want to import .csv file "data/AE_Attendances_Aug2010_Mar_2025.csv"
for files in os.listdir(data_folder):
    if files.endswith('.csv'):
        print(files)
    else:
        continue

# 1.4 Import .csv file "AE_Attendances_Aug2010_Mar_2025.csv"
Attendances_file = os.path.join('data','AE_Attendances_Aug2010_Mar_2025.csv')

AE_data = pd.read_csv(Attendances_file,
                      parse_dates=['Period'])

AE_data.info()
AE_data.head()
# 2. Split initial Set into TypeI, TypeII, TypeII with Period column datasets
# To apply later the adhoc trainsplit() function created in previous script:

AE_data_TypeIATT = AE_data[['Period','Type1_ATT']]
AE_data_TypeIIATT = AE_data[['Period','Type2_ATT']]
AE_data_TypeIIIATT = AE_data[['Period','Type3_ATT']]

print(AE_data_TypeIATT)

AE_data_TypeIATT.head()
AE_data_TypeIIATT.head()
AE_data_TypeIIIATT.head()

# 3.Exploratory plts

# 3.1 Load required seaborn and matplotlib libraries
import seaborn as sns
import matplotlib.pyplot as plt 
sns.set_theme(style="darkgrid")

# 3.1 Plot TypeIATT

# Dataset AE_data_TypeIATT
AE_data_TypeIATT.info()

# Get Min and Max dates for AE_data_TypeI DataFrame

# Min date 
Min_date_AE_data_TypeIATT = AE_data_TypeIATT['Period'].min()
print('Min period AE_data_TypeIATT dataframe is:',Min_date_AE_data_TypeIATT)

# Min period AE_data_TypeIATT dataframe is: 2010-01-08 00:00:00

# Max date
Max_date_AE_data_TypeIATT = AE_data_TypeIATT['Period'].max()
print('Max period AE_data_TypeIATT dataframe is:',Max_date_AE_data_TypeIATT)

# Max period AE_data_TypeIATT dataframe is: 2025-01-03 00:00:00

# 4 Plot AETypeIATT data by year

# 2011
AE_TypeIATT_2011 = AE_data_TypeIATT.loc[(AE_data_TypeIATT['Period'] >= '2011-01-01')
                                             & (AE_data_TypeIATT['Period'] <= '2011-01-12')]
# 2012
AE_TypeIATT_2012 = AE_data_TypeIATT.loc[(AE_data_TypeIATT['Period'] >= '2012-01-01')
                                             & (AE_data_TypeIATT['Period'] <= '2012-01-12')]

# Plot 2011 TypeIAtt data 

sns.set(rc={'figure.figsize':(10,5)})
ax = sns.lineplot(x='Period',y='Type1_ATT',data = AE_TypeIATT_2011, marker = '*', 
                  color = '#965786').set_title("UK TypeI Attendances Time series.2011 period")
# Plot 2012 TypeIAtt data 
sns.set(rc={'figure.figsize':(10,5)})
ax = sns.lineplot(x='Period',y='Type1_ATT',data = AE_TypeIATT_2012, marker = '*', 
                  color = '#965786').set_title("UK TypeI Attendances Time series.2012 period")