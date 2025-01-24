# File based on: "03_matplotlib_subplots.qmd" file
# File: 03_matplotlib_subplots.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2 * np.pi, 400)
y = np.sin(x ** 2)

# 1. Creating first subplot
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title('A single plot')

# 2. Stacking subplots in one direction

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)

# 3. Using our A&E data

# 3.1 First we load or data from .csv file
import pandas as pd
import os

wd = os.getcwd()
print(wd)

data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
print(data_folder)

AE_Attendances_file = r'c:\Users\OGTSLCEF\OneDrive - NHS\Documents\Python Scripts\data\AE_Attendances_2010_2024.csv'

AE_data = pd.read_csv(AE_Attendances_file,
parse_dates=[0],
                      date_format = '%d/%m/%Y')  

AE_data.head()

# 3.2 Then we rename existing columns to something meaningful
AE_data.columns = ['Date','Att_type1','Att_type2','Att_type3']
AE_data.columns
AE_data.head()

# 3.3 Use mkdir() method from OS module to create new folder to store output .png plots
os.mkdir("Plots")

# 3.4 Plot standard chart
import matplotlib.pyplot as plt

plt.title("Attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Date,AE_data.Att_type1)
plt.plot(AE_data.Date,AE_data.Att_type2)
plt.plot(AE_data.Date,AE_data.Att_type3)
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.savefig('Plots/Type I, II and IIII attendances 2010 2024 period_line_plot.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()

# 3.4 Plot chart as Subplots
fig, axs = plt.subplots(3)
fig.suptitle('TypeI, Type2, Type3 Attendances plot as Subplots')
axs[0].plot(AE_data.Date,AE_data.Att_type1)
axs[1].plot(AE_data.Date,AE_data.Att_type2)
axs[2].plot(AE_data.Date,AE_data.Att_type3)
plt.savefig('Plots/01 Type I, II and IIII attendances 2010 2024. Subplots.png', bbox_inches='tight')