# File based on: "02_matplotlib_bar_charts.qmd" file
# File: 02_matplotlib_bar_charts.py

# 1. Load required modules

import pandas as pd
import numpy as np
import os

# 2. Import data into Python from .csv 

wd = os.getcwd()
print(wd)

data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
print(data_folder)

AE_Attendances_file = r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\AE_Attendances_2010_2024.csv'

AE_data = pd.read_csv(AE_Attendances_file,
parse_dates=[0],
                      date_format = '%d/%m/%Y')  

AE_data.head()

# 3. Rename columns
AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']
AE_data.columns
AE_data.head()

# 4. Get AE_data dataframe info:
AE_data.info()
type(AE_data)


# 3. Use mkdir() method from OS module to create new folder to store output .png plots
os.mkdir("Plots")

# 4. Plot a line chart
# Save this plot into a sub-directory called "Plots". From os module we use .mkdir() method to create new **Plots** folder to save our output as .png files.

import matplotlib.pyplot as plt

### 1.1 Type I Attendances

# This first plot displays total number of AE Type 1 Attendances in England for the 2010-2024 period.
plt.title("Attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.plot(AE_data.Date,AE_data.Att_type2)
plt.plot(AE_data.Date,AE_data.Att_type3)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Plots/Type I, II and IIII attendances 2010 2024 period.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()

# 5. Bar plots in matplotlib 

# For this bar plot I will fist subset initial data to keep just TypeI attendances
AE_data.head()

# Subset data to keep just Type I Attendances 
AE_TypeI = AE_data[['Date','Att_type1']]
AE_TypeI.head()

### 5.1 Subset data for specific dates
AE_TypeI.set_index("Date",inplace=True)
AE_TypeI.head()

# Now that my Date column is defined as an index,  I can use .loc for label based indexing or .iloc for positional indexing.

AE_TypeI_AUG_OCT_2010 = AE_TypeI.loc['2010-08-01':'2010-10-01']
AE_TypeI_AUG_OCT_2010

### 5.2 Create bar chart for subset dat

AE_TypeI_AUG_OCT_2010.head()

# So I reset index using *reset_index()* method. 

AE_TypeI_AUG_OCT_2010.head()
AE_TypeI_AUG_OCT_2010_plot = AE_TypeI_AUG_OCT_2010.reset_index()
AE_TypeI_AUG_OCT_2010_plot

# Nowe we have just three months worth of daat in the above dataset, so I can create a small bar plot using matplotlib.
# Also I can save this bar plot in the Plots sub-folder I created earlier

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.bar(AE_TypeI_AUG_OCT_2010_plot.Date,
AE_TypeI_AUG_OCT_2010_plot.Att_type1)

ax.set_ylabel('Count of TypeI Attendances')
ax.set_title('Type I Attendances in England. Aug-Oct 2010')
ax.set_ylabel('Count of TypeI Attendances')
# Save chart in Plots sub-folder
plt.savefig('Plots/Type I, II and IIII attendances 2010 2024 period_bar_plot.png', bbox_inches='tight') ## This 
plt.show()