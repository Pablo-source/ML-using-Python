# We have downloaded several data Sources for Python that are Zipped files

# 1. Unzipping fies in Python using zipfile module

# DESCRIPTION
# Import the zipfile module, Create zip object using ZipFile class.
# Then call the extractall() method on zip file object 
# And pass the path where the files needed to be extracted 
# Finally extract the specific file present in the zip file

import pandas as pd
import os
from zipfile import ZipFile

mydir = os.getcwd()
mydir

print(mydir)

# Load  temp .zip file to create a zip object
# Zip file to unzip in the \data folder: stack-overflow-developer-survey-2022.zip

# 1.1 Open the zip file with the read mode 'r'
with ZipFile(r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\stack-overflow-developer-survey-2022.zip','r') as zObject:

# 1.1 Extracting all zip members into working directory
# using .extractall() method.
    zObject.extractall()
    
# 1.2 Extracting all zip members to a specific location
# I want to extract files to a new folder called "Survey_2022"
with ZipFile(r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\stack-overflow-developer-survey-2022.zip','r') as zObject:
    zObject.extractall(
        path = r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\Survey_2022'
    )
  
    
    
