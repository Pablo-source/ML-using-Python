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

#- I need to change default WD to ML-using-Python folder to access \data sub-folder to ingest Excel file called "INE total and foreign population figures Spain.xlsx"
ML_using_Python_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python')
print('My Python project folder is:',ML_using_Python_folder)

# change default folder to this /ML-using-Python folder
os.chdir(ML_using_Python_folder)
new_wd = os.getcwd()
print("Changed default working directory to:",new_wd)

# 3. Check data folder file contents
# - Check file contents from \data folder and build path to Excel file to be imported into python 
data_folder = os.path.join('/home','pablo','Documents','Pablo_zorin','VS_Python_GitHub_Pablo_source','ML-using-Python','data')
data_folder_contents = os.listdir(data_folder)
print('data folder contents:',data_folder_contents)

## 3.1 I want to import a .csv file for this script
# - Scan data_folder contents to list all .xlsx files. 
# # I want import "AE_Attendances_Aug2010_Mar_2025.csv" file that includes 
# # Attendances and Admissions for the 2010-2025 time period.
for files in os.listdir(data_folder):
    if files.endswith('.csv'):
        print(files)
    else:
        continue

# 4. Import Aug2010_Mar_2025 csv file into Python
# - From the above set of files, I want to import "AE_Attendances_Aug2010_mar_2025.csv" into 
# Python and split it into Type I Attendances, Type II Attendances and Type III Attendances, 
# as three independent .csv files, also I will create new variable 
# "Total Attendances" As the sum of the three existing columns.  
Attendances_file = os.path.join('data','AE_Attendances_Aug2010_Mar_2025.csv')
# Using parse_dates option
AE_data = pd.read_csv(Attendances_file, parse_dates=True)
AE_data.head()

AE_data.info()

# - Pandas package has not parsed Period as a Datime column. As it is defined as "object". 
# # Pandas interprets the Period column as strings.

## 4.1 Now I am using parse_dates to identify the specific column I want to parse as date from the CSV file 
# using parse_dates =['Period] option
AE_data_imported = pd.read_csv(Attendances_file,
                               parse_dates=['Period'])

# This new argument "parse_dates = ['Period']" correctly identifies the specific column to be parsed as date
# - Now "Period" column has successfully being imported into Python as a Date column
AE_data_imported.info()

# 5. Filter data from AE_data_imported based on a range of dates
# Filter data based on dates using DataFrame.loc[] function, the
# #  loc[] function is used to access a group of rows and columns of a 
# # DataFrame through labels or a boolean array.

# This will filter just 2011 data 
AE_data_imported_2011 = AE_data_imported.loc[(AE_data_imported['Period'] >= '2011-01-01')
                                             & (AE_data_imported['Period'] <= '2011-01-12')]
AE_data_imported_2011.head()

# Get Max date
Max_date_subset_data = AE_data_imported_2011['Period'].max()
print('Max period subset 2011 data is:',Max_date_subset_data)
# Get Min date
Min_date_subset_data = AE_data_imported_2011['Period'].min()
print('Min period subset 2011 data is:',Min_date_subset_data)



# 5. Plot Seaborn chart using 2011 AE Type3 Attendances data
AE_data_plot_2011 = AE_data_imported_2011.copy()

AE_data_plot_2011 = AE_data_plot_2011[['Period','Type3_ATT']]
AE_data_plot_2011.head()

# ### Plot Type3_ATT for 2011 subset period
sns.set(rc={'figure.figsize':(10,5)})
ax = sns.lineplot(x='Period',y='Type3_ATT',data = AE_data_plot_2011, marker = '*', color = '#965786').set_title("UK TypeIII Attendances. January-December 2011") 

#  Save Type3 Attendances 2011 data in "Seaborn_plots" folder
# This is the best way of importing .csv data into Python ensuring Date columns are imported as Datetime64 columns.

sns.set(rc={'figure.figsize':(10,5)})
ax = sns.lineplot(x='Period',y='Type3_ATT',data = AE_data_plot_2011, marker = '*', color = '#965786').set_title("UK TypeIII Attendances. January-December 2011") 
plt.savefig('Seaborn_gallery/Seaborn_plots/UK TypeIII Attendances UK.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()

# End of script: import_csv_into_Python_for_seaborn_plots.py
