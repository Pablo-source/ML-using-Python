#!/usr/bin/env python
# coding: utf-8
# # Adhoc functions
# This workbook includes several adhoc functions to be used on different scripts

import pandas as pd
import os
import matplotlib.pyplot as plt
import math

path = os.getcwd()
print(path)

# ### 1. Split initial data into Train and Test sets
# We have designed a function to split initial input data frame into Train and Test sets.
# The function has two parameters:
# - The data set you want to split defined by the "Inputdata" object
# - The percentage you want to assign to the Train split (usually 80%)

os.chdir('C:/Pablo UK/46 DATA SCIENCE all/10 ML python JULY 2021')
# Read in dataset

Sales = pd.read_csv('Sales_to_split_TRAIN_TEST.csv')
Sales.head()

# Function to split input data into train test sets
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

# Use above function
traintestsplitn(Sales, 80)

# Write output to csv files
train = pd.read_csv('TRAIN.csv')
train.head()
test = pd.read_csv('TEST.csv')
test.head()

# Check data type
print(isinstance(train, pd.DataFrame))
print(isinstance(test, pd.DataFrame))

# Check original file length matches TRAIN and TEST split
len(Sales)
len(train)
len(test)

len(train) + len(test)

# Function to check for the right length
def checksplit(main, train, test):
    """The length of input data set must match the sum of
    train and test sets length"""
    if len(main) == len(train) + len(test):
        print('The split has been successful')
    elif len(main) != len(train) + len(test):
        print('Try again')

# Use above function
checksplit(Sales, train, test)

# ## 3. Plot train and test series
# ** Important, set DATE as Index for both TRAIN and TEST sets**
train_plot = train.set_index('DATE')
train_plot.head()

test_plot = test.set_index('DATE')
test_plot.head()

plt.figure(figsize=(40, 20))
plt.title('Total sales')
plt.plot(train_plot, label="Train data")
plt.plot(test_plot, label="Test data")
plt.legend()
plt.ylabel("value")
plt.xlabel("years")
plt.tick_params(axis='x', which='major', labelsize=3)
plt.show()

# ## 4. Check distribution of each data sets
# #### 4.1  Train set
plt.figure(figsize=(20, 10))
plt.title('Total sales')
plt.plot(train_plot, label="Train data")
plt.legend()
plt.ylabel("value")
plt.xlabel("years")
plt.tick_params(axis='x', which='major', labelsize=3)
plt.show()

# #### 4.2  Test set
plt.figure(figsize=(20, 10))
plt.title('Total sales')
plt.plot(test_plot, label="Test data")
plt.legend()
plt.ylabel("value")
plt.xlabel("years")
plt.tick_params(axis='x', which='major', labelsize=3)
plt.show()
