
# Python script: 03_barplot.py

import numpy as np
import matplotlib.pyplot as plt

# Create  dataset

height = [3,4,54,17,40]
bars = ['A','B','C','D','E']

y_pos = np.arange(len(bars))

# Plot bars
plt.bar(y_pos, height)

# Include names on x axis 
plt.xticks(y_pos, bars)

# Display plot 
plt.show()_