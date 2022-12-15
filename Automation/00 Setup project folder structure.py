# import required libraries
import os
from os import path

wd = os.getcwd()
print(wd)

# Change current directory to Downloads folder
Downloads = '/home/pablo/Downloads'

Curr_dir = os.chdir(Downloads)

wd = os.getcwd()
print(wd)

# Create several folders to file and store away different file types

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

# Execute project_setup() function
project_setup()

