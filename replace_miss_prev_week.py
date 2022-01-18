# Function to replace missing value by same day previous week

for row in range(0, len(df3)):
    df3['value2'] = np.where(
        (np.isnan(df3['Sales'])) &
        (df3['File'] == df3['File'].shift(7)),

        df3['Sales'].shift(7), df3['Sales']
    )

# In[16]:
