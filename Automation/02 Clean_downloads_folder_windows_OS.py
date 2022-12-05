# AIM: Create a function to clean up Downloads folder, storing each file type on its own folder.
# Run it on a daily or weekly basis, to keep Download folder neat and tidy
# Date: 25/11/2022 |My Python and R weekly learning hour
# Last update: 30/11/2022
# Pablo Leon-Rodenas

# My notes:
# # IMPORTANT: remember to use double backslashes on the following lines
# Improvement: To avoid using two backslashes
# use r'' to enclose any path in Python
# Example
# download = r'C:\Users\Pablo.Leonrodenas\Downloads'
# xlsx_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.xlsx')
# target = r'C:\Users\Pablo.Leonrodenas\Downloads\01 xlsx_files'

import os
from os import path
import glob
import shutil

wd = os.getcwd()
print(wd)

# Linux download = '/home/pablo/Downloads'

# Windows work laptop
download = r'C:\Users\Pablo.Leonrodenas\Downloads'
os.chdir(download)


wd = os.getcwd()
print(wd)

# Section 01/02 project_setup builds required folders to store files in Downloads folder

# New function (improves performance)
# Combine folder creation and file moving into a single function.
# This new function is called: clean_downloadsfolder()


def clean_downloadsfolder():
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
    if not path.exists("09 pptx_files"):
        os.mkdir("09 pptx_files")
    if not path.exists("10 docx_files"):
        os.mkdir("10 docx_files")
    if not path.exists("11 py_files"):
        os.mkdir("11 py_files")
    if not path.exists("12 twbx_files"):
        os.mkdir("12 twbx_files")
    if not path.exists("13 twb_files"):
        os.mkdir("13 twb_files")

    print("Created project folder structure")


#  Section 02/02
#  Second section of this function Lists each of the file extensions in downloads folder
#  and moves it to its corresponding file extension folder

# 01/06 Excel 2013 files
    xlsx_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.xlsx')
    print(xlsx_files)
    print(len(xlsx_files))

    for item in range(len(xlsx_files)):
        print(xlsx_files[item])
# Now we move each .xlsx file to the previously created 01 xlsx_files folder
        original = xlsx_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\01 xlsx_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 01 xlsx_files folder")

# 02/06 PDF Files
    pdf_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.pdf')
    print(pdf_files)
    print(len(pdf_files))

    for item in range(len(pdf_files)):
        print(pdf_files[item])
    # Now we move each .pdf file to the previously created 02 pdf_files folder
        original = pdf_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\02 pdf_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 02 pdf_files folder")

# 03/06 Shapefile Files
    shp_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.shp')
    print(shp_files)
    print(len(shp_files))

    for item in range(len(shp_files)):
        print(shp_files[item])
    # Now we move each .shp file to the previously created 03 shp_files folder
        original = shp_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\03 shp_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 03 shp_files folder")

    # 04/06 CSV Files
    csv_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.csv')
    print(csv_files)
    print(len(csv_files))

    for item in range(len(csv_files)):
        print(csv_files[item])
    # Now we move each .csv file to the previously created 04 csv_files folder
        original = csv_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\04 csv_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 04 csv_files folder")

# 05/06 Jupyter notebooks
    jupyter_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.ipynb')
    print(jupyter_files)
    print(len(jupyter_files))

    for item in range(len(jupyter_files)):
        print(jupyter_files[item])
    # Now we move each .ipynb file to the previously created 05 ipynb_files folder
        original = jupyter_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\05 ipynb_files'
        shutil.move(original, target)
        print(f"file{item},has been moved to 05 ipynb_files folder")

# 06/06 Markdown Files
    markdown_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.html')
    print(markdown_files)
    print(len(markdown_files))

    for item in range(len(markdown_files)):
        print(markdown_files[item])
    # Now we move each .html file to the previouly created 06 Markdown_files folder
        original = markdown_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\06 Markdown_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 06 Markdown_files folder")

# 07/07 Old Excel files
    xls_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.xls')
    print(xls_files)
    print(len(xls_files))

    for item in range(len(xls_files)):
        print(xls_files[item])
    # Now we move each .html file to the previouly created 07 xls_files folder
        original = xls_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\07 xls_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 07 xls_files folder")

# 08 Deb files
    deb_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.deb')
    print(deb_files)
    print(len(deb_files))

    for item in range(len(deb_files)):
        print(deb_files[item])
    # Now we move each .html file to the previouly created 07 xls_files folder
        original = deb_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\08 deb_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 08 deb_files folder")

# 09 PPTX files
    pptx_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.pptx')
    print(pptx_files)
    print(len(pptx_files))

    for item in range(len(pptx_files)):
        print(pptx_files[item])
    # Now we move each .html file to the previously created 09 pptx_files folder
        original = pptx_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\09 pptx_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 09 pptx_files folder")

# 10 docx_files
    docx_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.docx')
    print(docx_files)
    print(len(docx_files))

    for item in range(len(docx_files)):
        print(docx_files[item])
    # Now we move each .html file to the previously created 10 docx_files folder
        original = docx_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\10 docx_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 10 docx_files folder")

# 11 py_files
    py_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.py')
    print(py_files)
    print(len(py_files))

    for item in range(len(py_files)):
        print(py_files[item])
    # Now we move each .html file to the previously created 11 py_files folder
        original = py_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\11 py_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 11 py_files folder")

# 12 twbx_files
    twbx_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.twbx')
    print(twbx_files)
    print(len(twbx_files))

    for item in range(len(twbx_files)):
        print(twbx_files[item])
    # Now we move each .html file to the previously created 12 twbx_files folder
        original = twbx_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\12 twbx_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 12 twbx_files folder")

# 13 twb_files
    twb_files = glob.glob(r'C:\Users\Pablo.Leonrodenas\Downloads\*.twb')
    print(twb_files)
    print(len(twb_files))

    for item in range(len(twb_files)):
        print(twb_files[item])
    # Now we move each .html file to the previously created 13 twb_files folder0
        original = twb_files[item]
        target = r'C:\Users\Pablo.Leonrodenas\Downloads\13 twb_files'
        shutil.move(original, target)
        print(f"file{item}, has been moved to 13 twb_files folder")

clean_downloadsfolder()