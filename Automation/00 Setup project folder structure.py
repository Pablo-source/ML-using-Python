# ## 1. Function to create project folder structure

wd = os.getcwd()
wd

Curr_dir = os.chdir('C:/Users/Pablo.Leonrodenas/Python_LEARNING')

os.mkdir("Project01")

New_dir = os.chdir('C:/Users/Pablo.Leonrodenas/Python_LEARNING/Project01')

# Import required libraries
import os.path
from os import path

# We can create several folders (data,Output,Shapefiles,model) within our Python project

def project_setup():
    if not path.exists("data"):
        os.mkdir("data")    
    if not path.exists("Shapefiles"):
        os.mkdir("Shapefiles")
    if not path.exists("model"):
        os.mkdir("model")
    if not path.exists("Output"):
        os.mkdir("Output")
    
    print("Created project folder structure")

project_setup()




