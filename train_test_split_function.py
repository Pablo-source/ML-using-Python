#!/usr/bin/env python
# coding: utf-8

# # Adhoc functions

# This workbook includes several adhoc functions to be used on different scripts

# In[1]:


import pandas as pd
import os


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


import math


# In[4]:


path = os.getcwd()
path


# ### 1. Split initial data into Train and Test sets

# We have designed a function to slpit initial input data frame into Train and Test sets. 

# The function has two paramters: 
# - The data set you want to split defined by the "Inputdata" object
# - The percentage you want to assign to the Train split (usuallt 80%)

# In[5]:


os.chdir('C:/Pablo UK/46 DATA SCIENCE all/10 ML python JULY 2021')


# Read in dataset

# In[6]:


Sales = pd.read_csv('Sales_to_split_TRAIN_TEST.csv') 
Sales


# In[8]:


import math


# In[7]:


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


# In[9]:


# Use above function
traintestsplitn(Sales, 80)


# ### Then we read in TRAIN and TEST files produced

# In[10]:


TRAIN = pd.read_csv('TRAIN.csv')
TRAIN


# In[11]:


TEST = pd.read_csv('TEST.csv')
TEST


# In[12]:


print(isinstance(TRAIN, pd.DataFrame))
print(isinstance(TEST, pd.DataFrame))


# ## 2. Check original file length matches TRAIN and TEST split

# In[13]:


len(Sales)
len(TRAIN)
len(TEST)


# In[14]:


len(TRAIN)+len(TEST)


# In[30]:


def chcksplit(main,traind,testd):
    if len(main)== len(traind)+len(testd):
        print('The split has been successful','second')
        
    elif len(main)!= len(traind)+len(testd):
         print('Try again')


# In[31]:


chcksplit(Sales,TRAIN,TEST)


# ## 3. Plot train and test series

# Function to check for the right lenght

# **Importnat, set DATE as Index for both TRAIN and TEST sets**

# In[32]:


TRAIN_plot = TRAIN.set_index('DATE')
TRAIN_plot


# In[33]:


TEST_plot = TEST.set_index('DATE')
TEST_plot.head()


# In[34]:


plt.figure(figsize=(40,20))
plt.title('Total sales')
plt.plot(TRAIN_plot, label = "Train data")
plt.plot(TEST_plot, label = "Test data")
plt.legend()
plt.ylabel("value")
plt.xlabel("years")
plt.tick_params(axis='x', which='major', labelsize=3)
plt.show()


# ## 4. Check distribution of each data sets

# #### 4.1  Train set

# In[35]:


plt.figure(figsize=(20,10))
plt.title('Total sales')
plt.plot(TRAIN_plot, label = "Train data")
plt.legend()
plt.ylabel("value")
plt.xlabel("years")
plt.tick_params(axis='x', which='major', labelsize=3)
plt.show()


# #### 4.2  Test set

# In[36]:


plt.figure(figsize=(20,10))
plt.title('Total sales')
plt.plot(TEST_plot, label = "Test data")
plt.legend()
plt.ylabel("value")
plt.xlabel("years")
plt.tick_params(axis='x', which='major', labelsize=3)
plt.show()


# In[ ]:




