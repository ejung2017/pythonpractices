import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

#iloc -> looks for the index (x value) vs loc -> y value
print(df.groupby('sex')['age'].idxmax())
"""
sex
female    275
male      630
Name: age, dtype: int64
"""
# female with index 275 has the max age and male with index of 630 has the max age 
# with this, we can look into the details of this particular person's data 

print(df.iloc[273])