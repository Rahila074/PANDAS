#REMOVING ROWS

#another way of handling wrong data.
#is to remove the rows that contain wrong data.

#this way you do not have to find out what to replace them with,
#and there is a good chance you do not need them to do your analyses.

#delete rows where  "Duration" is higher  than 60?

import pandas as pd

df = pd.read_csv('wrong.csv')

for x in df.index:
    if df.loc[x,"Duration"] > 60:
        df.drop(x,inplace=True)

print(df.to_string())