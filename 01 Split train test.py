# Load required libraries
import pandas as pd
import numpy as np
import os

# ### 1. Split initial data into Train and Test sets
# The function has two paramters:
# - The data set you want to split defined by the "Inputdata" object
# - The percentage you want to assign to the Train split (usuallt 80%)

def traintestsplitn(Inputdata, perctrain):
    """Split mean data set into train and test tests,
    TRAIN percent defined by user"""

    train_ceil = math.ceil(((len(Inputdata.index) * perctrain) / 100))
    train = Inputdata.iloc[0:train_ceil, ]

    train_output = pd.DataFrame(train)
    train_output.to_csv('TRAIN.csv', index=False)

    test = Inputdata.iloc[train_ceil:, ]
    test_output = pd.DataFrame(test)
    test_output.to_csv('TEST.csv', index=False)
    return train_output, test_output

# Use the above function
traintestsplitn(Sales, 80)

import math

# ##### 1.2. Ensure the split has been successful
def chcksplit(main, traind, testd):
    if len(main) == len(traind) + len(testd):
        print('The split has been successful')
    elif len(main) != len(traind) + len(testd):
        print('Try again')

chcksplit(Sales, TRAIN, TEST)