### 1. Load libraries to input data into Python
import pandas as pd
import numpy as np
import os

### 1. List files in \data sub-folder
wd = os.getcwd()
print(wd)
data_folder = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data'
print(data_folder)

# List files in my /data folder
data_folder_contents = os.listdir(data_folder)
print(data_folder_contents)


### 2. Import AE Attendances data from \data sub-folder 

AE_Attendances_file = r'/home/pablo/Documents/Pablo_zorin/VS_Python_topics/data/AE_Attendances_2010_2024.csv'
AE_data = pd.read_csv(AE_Attendances_file,
parse_dates= [0],
date_format='%d/%m/%Y')
AE_data.head()


# 3. Load Matplotlib library 
from matplotlib import pyplot as plt

### 3.1 Include legends in matplotlib plots

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
plt.savefig('Type I, II and IIII attendances 2010 2024 period.png', bbox_inches='tight') ## Save plot as .png file


# 3.2 Save plot in a new "Plots" sub-folder
plt.title("Total attendances by Type (I,II,III) in England.2010-2024 Period")
plt.plot(AE_data.Period,AE_data.Type1_ATT, label = "Type I Attendences")
plt.plot(AE_data.Period,AE_data.Type2_ATT, label = "Type II Attendences")
plt.plot(AE_data.Period,AE_data.Type3_ATT, label = "Type III Attendences")
plt.xlabel("Time")
plt.ylabel("Attendances")
plt.legend(loc="lower left")
# Save this new line chart in a Plots sub-folder
plt.savefig('Plots/Type I, II and IIII attendances 2010 2024 period.png', bbox_inches='tight') ## Save plot as .png file

## 3.3 Create a new plot using numpy to display sin and cos function
# Save it in the Plots sub-folder

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,1000)
print(x)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title('Sin and cos functions using numpy')
plt.plot(x,y1, "-r", label = "Sine")
plt.plot(x,y2, "-b", label = "Cosine")
plt.legend(loc = "upper left")
plt.ylim(-1.5,2.0)
plt.savefig('Plots/Sin and Cos function example.png', bbox_inches='tight') ## Save plot in the \Plots sub-folder
plt.show()