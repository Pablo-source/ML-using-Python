### 1. Load libraries to input data into Python
import pandas as pd
import numpy as np
import os

### 1. List files in \data sub-folder
wd = os.getcwd()
print(wd)
data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
print(data_folder)

# List files in my /data folder
data_folder_contents = os.listdir(data_folder)
print(data_folder_contents)


### 2. Import AE Attendances data from \data sub-folder 

AE_Attendances_file = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data/AE_Attendances_2010_2024.csv'
AE_data = pd.read_csv(AE_Attendances_file,
parse_dates= [0],
date_format='%d/%m/%Y')
AE_data.head()