# This is a workbook to practise Matplotlib library. To create all type of plots
# File: 01_matplotlib_line_dots_plots.py 
# 
# Date: 12/01/2025

### 1. Load libraries to input data into Python
import pandas as pd
import numpy as np
import os

### 2. Ingest data into Python from \data folder
wd = os.getcwd()
print(wd)
data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
print(data_folder)

# List files in my /data folder
data_folder_contents = os.listdir(data_folder)
print(data_folder_contents)

# ['wine_quality.zip', 'winequality.names', 'winequality-red.csv', 'Survey_2024', 'stack-overflow-developer-survey-2024.zip', 'stack-overflow-developer-survey-2022', 'Matplotlib', 
# #  'AE_Attendances_2010_2024.csv', 'stack-overflow-developer-survey-2020', 'winequality-white.csv', 'monthly-milk-production-pounds.csv']

### 3. Matplotlib example

## 3.1 Import pyplot module from matplotlib library
from matplotlib import pyplot as plt

x = [2,3,4]
y = [1,4,8]
z = [11,6,0]

# 3.2 Basic plot of two series with titles and legend
plt.plot(x,y)
plt.plot(x,z)
plt.title("Line chart, x and z variables")
plt.xlabel("x")
plt.ylabel("x and z vars")
plt.legend(["This is Y variable","This is Z variable"])
plt.savefig('Basic matplotlib plot.png', bbox_inches='tight') ## This saves the output plot
plt.show()

AE_Attendances_file = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data/AE_Attendances_2010_2024.csv'

# 4. Import data first not formattting date
AE_data = pd.read_csv(AE_Attendances_file)

AE_data.head()
AE_data.columns
AE_data.info()


# Rename column names using .columns
# New column names: Date, Att_type1, Att_type2, Att_type3
AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']

# Check individual column values
AE_data.Att_type1
AE_data.Att_type2
AE_data.Att_type3

type(AE_data.Att_type1)

# Check first ans third values
AE_data.Att_type1[0]
AE_data.Att_type1[2]


# 4.1 Plot Att_type1 and Att_type2 values on the same chart
plt.plot(AE_data.Att_type1,AE_data.Att_type2)
plt.show()
# This is a line chart, it makes more sense to plot it using dots as continuous measures
plt.plot(AE_data.Att_type1,
         AE_data.Att_type2,'o')
plt.title("Scatterplot, Att Type 1 against Att Type 2")
plt.xlabel("Att Type 2")
plt.ylabel("Att Type 1")
plt.show()

### 4.2 Plotting two columns on different plot lines
# We can also combine two different columns on diffeerntn plots. By using diffeernt plt.plot() statements
#  for each series or column.
# - To obtain **two lines** we need to use two **different** plt.plot() statements.

# 4.2.1 Sample plot including two lines
my_data = {
    'column_a':[1,2,3,4,5],
    'column_b':[1,4,9,16,25],
    'column_c':[10,8,6,4,2]
}

# We have just created a dictionary 
type(my_data)
# Turn it into a dataframe
my_data_frame = pd.DataFrame(my_data)

# 4.2.1 Line chart with two series 
plt.plot(my_data_frame.column_a,my_data_frame.column_b)  # First line from column B
plt.plot(my_data_frame.column_a,my_data_frame.column_c)  # Second line from column C
plt.title("Scatterplot, Including two series")
plt.xlabel("a")
plt.ylabel("b and c columns")
# Include now legend
plt.legend(["this is b","this is c"])
plt.savefig('Basic matplotlib line plot.png', bbox_inches='tight') ## This saves the output plot
plt.show()

# 4.2.2 dot chart with with two series
# Include 'o' on each plt.plot() statement
plt.plot(my_data_frame.column_a,my_data_frame.column_b,'o')  # First line from column B
plt.plot(my_data_frame.column_a,my_data_frame.column_c,'o')  # Second line from column C
plt.title("Scatterplot, Including two series")
plt.xlabel("a")
plt.ylabel("b and c columns")
# Include now legend
plt.legend(["this is b","this is c"])
plt.savefig('Basic matplotlib dot plot.png', bbox_inches='tight') ## This saves the output plot
plt.show()


# 5. Import csv file and format date variables 

AE_Attendances_file = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data/AE_Attendances_2010_2024.csv'

# 5.1. Import data first not formattting date
AE_data_raw = pd.read_csv(AE_Attendances_file)

AE_data_raw.head()
AE_data_raw.columns
AE_data_raw.info()

AE_data_raw.head()

# We can see how the plot does not have formatted dates
plt.title("TypeI Attendances in England.2010-2024 Period")
plt.plot(AE_data_raw.Period,
AE_data_raw.Type1_ATT)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Example plot date not formatted.png', bbox_inches='tight') ## This saves the output plot
plt.show()

# 5.2 Import csv file formatting date variables
# - parse_dates =[0]  (Dates defined as Rows, or date variables is on the first column)
# - date_format = '%d/%m/%Y' (incomind date format)

AE_data = pd.read_csv(AE_Attendances_file,
                    parse_dates= [0],
                    date_format='%d/%m/%Y')
AE_data.head()

# As you can see, now the date is correctly formatted to be plotted in a chart
plt.title("Attendances TypeI in England. 2010-2024 period")
plt.plot(AE_data.Period,
AE_data.Type1_ATT)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Type I attendances 2010-2013 period.png', bbox_inches='tight') ## This saves the output
plt.show()

# Type1 and Type2 line chart Attendances in England. 2010 2014 period.
plt.title("Attendances TypeI in England.2010-2024 Period")
plt.plot(AE_data.Period,AE_data.Type1_ATT)
plt.plot(AE_data.Period,AE_data.Type2_ATT)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Type I and II attendances 2010 2024 period.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()

# Type1, Type2 and Type3 Attendances  line chart Attendances in England. 2010 2014 period.
plt.title("Total attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Period,AE_data.Type1_ATT)
plt.plot(AE_data.Period,AE_data.Type2_ATT)
plt.plot(AE_data.Period,AE_data.Type3_ATT)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Type I, II and IIII attendances 2010 2024 period.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()

### 6. Include legends in matplotlib plots
## Include legend to each plt.plot() function label Type I Attendances
# plt.legend(loc='best')
# plt.legend(loc="upper left")
plt.title("Total attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Period,AE_data.Type1_ATT, label = "Type I Attendences")
plt.plot(AE_data.Period,AE_data.Type2_ATT, label = "Type II Attendences")
plt.plot(AE_data.Period,AE_data.Type3_ATT, label = "Type III Attendences")
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.legend(loc="lower left")
plt.savefig('Type I, II and IIII attendances 2010 2024 period.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()
