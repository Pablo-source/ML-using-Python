import pandas as pd

# ## 6.Function to lag data to multiple regression X features
# ### For a recurrent neural network the order of theTrain Features X_tran dataframe must be t-5,t-4,t-3,t-2,t-1

def get_features(data, total_lags):
    columns = []
    for each_lag in range(total_lags, 0, -1):
        Lag_i = pd.DataFrame(data.shift(each_lag + 1, axis=0, fill_value=0))
        columns.append(Lag_i)
    features = pd.concat(columns, axis=1)
    # Include column labels
    labfeatures = features.copy()
    N_cols = len(labfeatures.columns)
    col_list = ['Sales t-' + str(x) for x in range(N_cols, 0, -1)]
    labfeatures.columns = col_list
    # remove rows including zero values
    trunc_feat = labfeatures.iloc[total_lags:]
    return trunc_feat


get_allfeatures(data, total_lags):

# The data input dataset is the scales Traindata_scaled Series we defined earlier. This is the features dataset X_train that is a reversed dataframe ['Sales t-5', 'Sales t-4', 'Sales t-3', 'Sales t-2', 'Sales t-1']
X_train_rev = get_features(Traindata_scaled, total_lags)
X_train_rev