
# 02 EDA from csv filepy
# 1. Load required libraries 
import pandas as pd
import numpy as np
import os

# 2. Ingest dataset from \data folder 
wd = os.getcwd()
print(wd)

# CSV.file: monthly-milk-
data_folder = os.listdir(r'/home/pablo/Documents/Pablo_zorin/VS_Python_TUTORIALS/data/monthly-milk-production-pounds.csv')
print(data_folder)

# 2.1 Format date column 
# 2.1.1 Define Date column as Index in your dataframe
# Now, let's set the Date column as a dataframe index using the set_index method:

# 2.1.2 Then use parse_dates to display date format correctly YYYY-MM-DD
milk_production  = '/home/pablo/Documents/Pablo_zorin/VS_Python_TUTORIALS/data/monthly-milk-production-pounds.csv'
df = pd.read_csv('/home/pablo/Documents/Pablo_zorin/VS_Python_TUTORIALS/data/monthly-milk-production-pounds.csv'
                 , index_col = 'Date', parse_dates= True)

df.head()
df.columns

# Get df properties
df.info()
df.dtypes

dtypes = df.dtypes.to_dict()
print(dtypes)

# 3. Plot data  
# https://www.datacamp.com/tutorial/matplotlib-time-series-line-plot
import matplotlib.pyplot as plt
import numpy as np

plt.plot(Date,Production)
plt.show()

# Creating a basic single-line matplotlib time series plot
# To create a basic time series line plot, we use the standard matplotlib.pyplot.plot(x, y) method:

plt.plot(df.index, df['Production'])
plt.show()

# To create a multiple-line time series plot, we just run the matplotlib.pyplot.plot(x, y) method the necessary number of times: 
# In case there were three series [CAD,NZD,USD]
# plt.plot(df.index, df['CAD'])
# plt.plot(df.index, df['NZD'])
# plt.plot(df.index, df['USD'])