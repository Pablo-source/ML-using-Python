# Load required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
import numpy as np

# Seaborn libraries
import seaborn as sns
sns.set_theme(style = "darkgrid")

num_rows = 20
years = list(range(1900, 1900 + num_rows))

data_wide = pd.DataFrame(
    {
        'Year':years,
        'A': np.random.randn(num_rows).cumsum(),
        'B': np.random.randn(num_rows).cumsum(),
        'C': np.random.randn(num_rows).cumsum(),
        'D': np.random.randn(num_rows).cumsum(),
    }
)

data_wide.info()
data_wide.head()

# Convert dataframe from wide to long
df_long = pd.melt(data_wide,['Year'])
df_long.info()
df_long.head()

my_wd = os.getcwd()
print(my_wd)

# Then plot multiple lines into a single chart
sns.lineplot(data = df_long , x ='Year', y = 'value', hue = 'variable').set_title("Seaborn Multiple line chart example")
plt.savefig('/home/pablo/Documents/Pablo_zorin/VS_Python_GitHub_Pablo_source/ML-using-Python/Seaborn_gallery/Seaborn_plots/Multiple line chart example.png', bbox_inches='tight') ## This saves the output plot successfully in the project folder
plt.show()