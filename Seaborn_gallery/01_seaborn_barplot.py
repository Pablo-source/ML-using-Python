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

# 5. Use String slice to create Year variable from date column

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


# 6. Subset variables and create Seaborn barplot 
# Subset just three columns from previous Data Frame: two main metrics
# #  "Total_Population", "Foreign_population" and newly created "Year" column. Also when subsetting those columns
# #  I want to place Year as the first column on the left.

INE_foreign_pop_plot = INE_total_foreign_population[['Year','Total_population','Foreign_population']]
INE_foreign_pop_plot.head()

# 7. Create first Seaborn barplot 

# 7.1 Sort data in ascending order for bar plot
INE_first_plot = INE_foreign_pop_plot.head(21)
INE_first_plot

INE_first_plot.sort_values(by='Year',ascending = True) # Sort dataframe ascending order by Year column

INE_first_plot.head() 


# 7.2 First Unformatted Seaborn bar plot
sns.set_theme()

plt.figure(figsize=(3, 3))
plt.rcParams["figure.figsize"] = (25, 15)
sns.barplot(data = INE_first_plot_sorted,
            x = "Year", 
            y = "Total_population",log = False).set_title("Spain total population.2005-2025 period")
plt.show()

# 7.3 Seaborn barplot formatted plot
# Apply format to Y axis numbers to avoid scientific default notation
from matplotlib.ticker import ScalarFormatter

sns.set_theme()
fig = plt.figure(figsize=(30, 15))
axs = fig.add_subplot(1, 1, 1)
sns.barplot(data = INE_first_plot_sorted,
            x = "Year", 
            y = "Total_population").set_title("Spain total population.2005-2025 period")
formatter = ScalarFormatter()
formatter.set_scientific(False)
axs.yaxis.set_major_formatter(formatter)
plt.show()

# 7.4 Save seaborn barplot as png file 

# Save figure as Seaborn barplot, this is an example of a Seaborn bar plot with y axis formatted
# Also the output plot will be saved as .png file in the Seaborn_plots sub-folder
# Output: .png image saved inside Seaborn_gallery/Seaborn_plots folder

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

sns.set_theme()
fig = plt.figure(figsize=(30, 15))
axs = fig.add_subplot(1, 1, 1)
sns.barplot(data = INE_first_plot_sorted,
            x = "Year", 
            y = "Total_population").set_title("Spain total population.2005-2025 period")
formatter = ScalarFormatter()
formatter.set_scientific(False)
axs.yaxis.set_major_formatter(formatter)
plt.savefig('Seaborn_gallery/Seaborn_plots/Spain total population 2005-2025 period.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()
