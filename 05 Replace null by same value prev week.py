# ## 5.Replace null values by same day previous week non-null value
import numpy as np

for row in range(0, len(SalesQ)):
    SalesQ['Eastbranch'] = np.where(
        (np.isnan(SalesQ['Eastbranch'])),
        SalesQ['Eastbranch'].shift(7), SalesQ['Eastbranch']
    )