# ## 3.Function to lag data to multiple regression X features
# -> total_lags in your initial case was 7
# -> initial empty list that we append elements inside of
# -> loops over the input value total_lags. If total_lags = 7 then range(total_lags)= [1,2,3,4,5,6,7]
# -> same as your line: pd.concat([Lag1,Lag2,Lag3,Lag4,Lag5,Lag6,Lag7],axis=1)

import pandas as pd
import numpy as np
import os

def get_allfeatures(data, total_lags):
    list_of_columns = []
    for time_lag in range(total_lags):
        Lag_i = pd.DataFrame(data.shift(time_lag + 1, axis=0, fill_value=0))
        list_of_columns.append(Lag_i)
    features_array = pd.concat(list_of_columns, axis=1)
    return features_array

get_allfeatures(data_set, 7)