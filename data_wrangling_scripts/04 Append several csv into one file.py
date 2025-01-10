# ## 4.Function to combine several csv files into one using Pandas
import pandas as pd
import numpy as np
import os

next(os.walk('.'))[1]

files = [file for file in os.listdir('./Sales_Data')]
files

all_months = pd.DataFrame()
all_months

for file in files:
    dfc = pd.read_csv("./Sales_Data/" + file)
    all_months = pd.concat([all_months, dfc])

# Outside the  loop we write the combined dataframes into a .csv
all_months.to_csv("all_months.csv", index=False)

def append_csvfiles():
    next(os.walk('.'))[1]
    files = [file for file in os.listdir('./Sales_Data')]
    all_months = pd.DataFrame()
    for file in files:
        dfc = pd.read_csv("./Sales_Data/" + file)
        all_months = pd.concat([all_months, dfc])
    all_months.to_csv("all_months.csv", index=False)

append_csvfiles()