
# Python script: 03_barplot_using_AE_data.py

# 1. Load required modules

import pandas as pd
import numpy as np
import os

# 2. Import data into Python from .csv 

wd = os.getcwd()
print(wd)

data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/data'
print(data_folder)

AE_Attendances_file = r'/home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/data/AE_Attendances_2010_2024.csv'
print(AE_Attendances_file)

AE_data = pd.read_csv(AE_Attendances_file,
pxarse_dates=[0],
                      date_format = '%d/%m/%Y')  

AE_data.head()

# 3. Rename columns
AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']
AE_data.columns
AE_data.head()

# 4. Get AE_data dataframe info:
AE_data.info()
type(AE_data)

# 5. Bar plots in matplotlib 

# Subset data to keep just Type I Attendances 
AE_TypeI = AE_data[['Date','Att_type1']]
AE_TypeI.head()

### 5.1 Subset data for specific dates
AE_TypeI.set_index("Date",inplace=True)
AE_TypeI.head()

# 5.2 Now that my Date column is defined as an index,  I can use .loc for label based indexing or .iloc for positional indexing.
# Subset  Aug, Sep, Oct 20210 data for this bar plot 
AE_TypeI_AUG_OCT_2010 = AE_TypeI.loc['2010-08-01':'2010-10-01']
AE_TypeI_AUG_OCT_2010

### 5.3 Create bar chart for subset data
# To create the bar chart I need to reset index, as I have setup Date as index
# to slice my data 
AE_TypeI_AUG_OCT_2010.head()
AE_TypeI_AUG_OCT_2010_plot = AE_TypeI_AUG_OCT_2010.reset_index()
AE_TypeI_AUG_OCT_2010_plot.head()

# Now the data is ready to be used in matplotlib to create a bar plot

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# We create a barplot using .bar() function 
ax.bar(AE_TypeI_AUG_OCT_2010_plot.Date,
       AE_TypeI_AUG_OCT_2010_plot.Att_type1)

ax.set_ylabel('Count of TypeI attendances')
ax.set_xlabel("Date")
ax.set_title("Type I Attendances in England. Aug-Oct 2010")
# Saving bar chart in plots sub-folder
plt.savefig('Plots/Bar_plot_TypeI_Attendances_England_Aug_Oct_2010.png', bbox_inches='tight')
plt.show()
