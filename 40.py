#LOOP through all values in the "Duration" column.

#if the value is higher than 60, set it to 55:

import pandas as pd

df = pd.read_csv('wrong.csv')

for x in df.index:
    if df.loc[x,"Duration"] > 60:
       df.loc[x,"Duration"] = 55

print(df.to_string())