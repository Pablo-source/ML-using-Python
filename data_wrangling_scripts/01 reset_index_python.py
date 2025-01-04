# Populate this script with the contents from "07 01_Reset_index_python.ipynb" notebook

# - In Python, indexing refers to the process of accessing a specific element in a sequence, such as a string or a list. Using its position or index number. 
# - Indexing in Python **starts at 0**, which means that the **first** element in a sequence has an **index** of **0**, the **second** element has an **index of 1** and so on 

import os



# >> 1. Download and UNZIP data from UC Irvine Machine Learning to pracise index manipulations <<
#   https://archive.ics.uci.edu/dataset/186/wine+quality


# Check first our working directory
wd = os.getcwd()
wd

# 2. We will use zipfile function to extract files included in a zip file called "wine_quality.zip"
# saved in the data folder
# 
os.listdir(r'/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data')


#- First we import zipfile module
#- Then we create a zip file object using ZipFile class
#- Then we call the extrtactall() method on zip file object and pass the path where the files needded to be exrtacted
#- Extract all files present in the zip file

from zipfile import ZipFile

# Load the temp .zip and create a zip object
with ZipFile(r'/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data/wine_quality.zip','r') as zObject:
# Extract all contents from the zipped file to a specific location 
# We use extractall() method on that zObject we have just created
    zObject.extractall(
        path= r'/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data'
)
    
# Now we can see how two new .csv files about wine quality have been extracted to the /data folder
os.listdir(r'/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data')

# We can specifically search for .csv files. We need to use the glob method
import glob
# Path to search files inside a specific sub-folder
# We specify the file extension (*.csv) we want to search inside our project folder
path = r'/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data/*.csv'
files = glob.glob(path)
print(files)


# >> 2. Import White wine data set into Python <<
import pandas as pd

white_wine = pd.read_csv(r"/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data/winequality-white.csv",sep =";")

white_wine.head()


# >> 2.1 Get white wine dataset details 

print(white_wine)   # 1.Get dataset overview
white_wine.info()   # 2. Get dataset details
print(white_wine.columns) # 3. Get dataset column names

# 2.2 Create new variables 

# To create new variables in Python we first specify the data frame where we want 
# # to create the new varible and then we specify the new variable in square brackets and write its
# #  new name in commas, then we use = sign to assign the specific value to the new variable we've just created

# 2.2.1 For example, to create a new variable called 'is_red' that takes value 0 in the white_wine data frame we will do it this way: 
white_wine['is_red']=0.0

# We can see how the new variable 'is red' has been created in our original data frame when using .info() method
white_wine.info()

# 2.2.2 For example, to create a new variable called 'is_white' that takes value 1 in the white_wine data frame we will do it this way: 
white_wine['is_white']=1.0

white_wine.head()
white_wine_checks = white_wine.copy()
white_wine_checks.head()

#### 2.3 Subset variables from DataFrame

# 2.3.1 To select a single column 
#Each *column* in a *DataFrame* is a *Series*. As a single column is selected, the returned object is a pandas **series**

One_col = white_wine_checks["quality"]
One_col

# We can check how this is a *Series* unidimensional object
type(white_wine_checks["quality"])
white_wine_checks["quality"].shape
# (4898,)

# 2.3.2 To select multiple columns
# To select **multiple** columns, you use a **list of columns** names **within** the selection brackets []
# So you apply this principle. To subset columns from a data frame, we enclose the list of columns we want to subset from the original data frame into square brackets []

white_subset = white_wine_checks[['quality','is_red','is_white']]
white_subset.head()

type(white_subset) # This is a dataframe because we have selected several columns

# The above Data frame is made of just **Three** columns from the original data frame

### 3. Import Red wine data set into Python 
#### And create two same new variables "is_red" and "is_white"

import pandas as pd

red_wine = pd.read_csv("/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data/winequality-red.csv",sep =";")
red_wine.head()
red_wine.info()

# Create two new variables in this red_wine data setL: 'is red' equals to 0.0 and 'is white' equals to 1.0

red_wine['is_red'] = 0.0
red_wine['is_white'] = 1.0

# Now we check the two new variables in our red_wine data frame
red_wine.info()

# ### 4. Concatenate both red_wine and white_wine dataframes

# We use function pd.concat() to concatenate two data frames

# - It takes two arguments:
#    - **pd.concat([dataframeA,dataframeB,axis])**
#    - First the data frames we want to concatenate as a list [dataframeA,dataframeB]
#    - Then the axis, how to concatenate the data frames

#- In Pandas: 
#    - axis = 0 refers to horizontal axis or *ROWS*
#    - axis = 1 refers to vertical axis or *COLUMNS*

white_wine.info()
len(white_wine)

red_wine.info()
len(red_wine)

# We use pd.concat() with **axis =0** as we want to stack our data in ROWS, one on top of the other. To Union data frames in Python we use **axis = 0**  
# Total length we will obtain after concatenating them
# Total = 4898 + 1599

#    - axis = 0 refers to horizontal axis or *ROWS*
# We have same number of columns or variables in our dataframes, so we can union them. When using .info() argument we have seen that in both instances we have 14 columns 
all_wine = pd.concat([white_wine,red_wine],axis =0)
all_wine.head()

all_wine.tail()

# We can see that he total number of rows 1598 **DOES NOT MATCH** the sum of individual rows from Dataframe white_wine and red_wine.
# #  This is a case then we have to **reset the index**

### 5. Reset index in our merged Dataframe

# There are a few reasons why we might want to reset the index of a pandas dataframe:

# 1. **Missing or duplicate index values**: Sometimes, the index values might be missing or duplicated. In such cases, resetting the index can help to reassign new index values to the dataframe.

# 2. **Change the order of rows**: By default, the rows in a dataframe are ordered by their index values. If we want to change the order of rows based on some other criteria, resetting the index can help to sort the rows based on a different column.

# 3. **Merge or join dataframes**: When we merge or join two or more dataframes, we might end up with duplicate index values. Resetting the index can help to avoid such conflicts.

# As we have UNIONED two data frames, we will recommend to reset the index of the merged dataframe

all_wine.tail()

# We use method .reset_index() to reset an index of the Pandas dataframe. To avoid duplicated indexes, is always recommended to include (drop = True) when using that method
all_wine_reset = all_wine.reset_index(drop = True)
all_wine_reset.head()
all_wine_reset.tail()

# Now we have our dataframe with the right index after we have performed a union of both red and white sets
# The final step will be to export this new dataframe as a .csv file names "all_wine_reset.csv"

all_wine_reset.to_csv(r"/home/pablo/Documents/Pablo_zorin/VS_Python_projects/data/all_wine_reset.csv")
