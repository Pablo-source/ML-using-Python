
# Python script: 03_barplot.py

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

