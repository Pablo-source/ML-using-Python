
# AIM: Create a function to clean up Downloads folder, storing each file type on its own folder.
# Run it on a daily or weekly basis, to keep Download folder neat and tidy
# Pablo Leon-Rodenas

import os
from os import path
import glob
import shutil

wd = os.getcwd()
print(wd)

download = '/home/pablo/Downloads'

os.chdir(download)

wd = os.getcwd()
print(wd)

# Section 01/02 project_setup builds required folders to store files in Downloads folder

# New function (improves performance)
# Combine folder creation and file moving into a single function.
# This new function is called: clean_downloadsfolder()


def clean_downloadsfolder():
# Create new directories in your Downloads folder to save each individual file extension 
    if not path.exists("01 xlsx_files"):
        os.mkdir("01 xlsx_files")
    if not path.exists("02 pdf_files"):
        os.mkdir("02 pdf_files")
    if not path.exists("03 shp_files"):
        os.mkdir("03 shp_files")
    if not path.exists("04 csv_files"):
        os.mkdir("04 csv_files")
    if not path.exists("05 ipynb_files"):
            os.mkdir("05 ipynb_files")
    if not path.exists("06 Markdown_files"):
        os.mkdir("06 Markdown_files")
    if not path.exists("07 xls_files"):
        os.mkdir("07 xls_files")
    if not path.exists("08 deb_files"):
        os.mkdir("08 deb_files")
    print("Created project folder structure")

#  Section 02/02
#  Second section of this function Lists each of the file extensions in downloads folder
#  and moves it to its corresponding file extension folder

# 01/06 Excel 2013 files
    xlsx_files = glob.glob('/home/pablo/Downloads/*.xlsx')
    print(xlsx_files)
    print(len(xlsx_files))

    for item in range(len(xlsx_files)):
        print(xlsx_files[item])
# Now we move each .xlsx file to the previously created 01 xlsx_files folder
        original = xlsx_files[item]
        target = r'/home/pablo/Downloads/01 xlsx_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 01 xlsx_files folder")

# 02/06 PDF Files
    pdf_files = glob.glob('/home/pablo/Downloads/*.pdf')
    print(pdf_files)
    print(len(pdf_files))

    for item in range(len(pdf_files)):
        print(pdf_files[item])
    # Now we move each .pdf file to the previously created 02 pdf_files folder
        original = pdf_files[item]
        target = r'/home/pablo/Downloads/02 pdf_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 02 pdf_files folder")

# 03/06 Shapefile Files
    shp_files = glob.glob('/home/pablo/Downloads/*.shp')
    print(shp_files)
    print(len(shp_files))

    for item in range(len(shp_files)):
        print(shp_files[item])
    # Now we move each .shp file to the previously created 03 shp_files folder
        original = shp_files[item]
        target = r'/home/pablo/Downloads/03 shp_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 03 shp_files folder")

    # 04/06 CSV Files
    csv_files = glob.glob('/home/pablo/Downloads/*.csv')
    print(csv_files)
    print(len(csv_files))

    for item in range(len(csv_files)):
        print(csv_files[item])
    # Now we move each .csv file to the previously created 04 csv_files folder
        original = csv_files[item]
        target = r'/home/pablo/Downloads/04 csv_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 04 csv_files folder")

# 05/06 Jupyter notebooks
    jupyter_files = glob.glob('/home/pablo/Downloads/*.ipynb')
    print(jupyter_files)
    print(len(jupyter_files))

    for item in range(len(jupyter_files)):
        print(jupyter_files[item])
    # Now we move each .ipynb file to the previously created 05 ipynb_files folder
        original = jupyter_files[item]
        target = r'/home/pablo/Downloads/05 ipynb_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 05 ipynb_files")

# 06/06 Markdown Files
    markdown_files = glob.glob('/home/pablo/Downloads/*.html')
    print(markdown_files)
    print(len(markdown_files))

    for item in range(len(markdown_files)):
        print(markdown_files[item])
    # Now we move each .html file to the previouly created 06 Markdown_files folder
        original = markdown_files[item]
        target = r'/home/pablo/Downloads/06 Markdown_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 06 Markdown_files")

# 07/07 Old Excel files
    xls_files = glob.glob('/home/pablo/Downloads/*.xls')
    print(xls_files)
    print(len(xls_files))

    for item in range(len(xls_files)):
        print(xls_files[item])
    # Now we move each .html file to the previouly created 07 xls_files folder
        original = xls_files[item]
        target = r'/home/pablo/Downloads/07 xls_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 07 xls_files")

# 08 Deb files
    deb_files = glob.glob('/home/pablo/Downloads/*.deb')
    print(deb_files)
    print(len(deb_files))

    for item in range(len(deb_files)):
        print(deb_files[item])
    # Now we move each .html file to the previouly created 07 xls_files folder
        original = deb_files[item]
        target = r'/home/pablo/Downloads/08 deb_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 08 deb_files")


clean_downloadsfolder()

