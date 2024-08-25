#pivot tables

import pandas as pd

#create a Dataframe

data = {
    'name':['alice','bob','charlie','david','eva'],
    'age':[24,27,22,32,29],
    'city':['new york','los angles','chicago','houstan','phonix'],
    'salary':[50000,60000,55000,65000,70000]
}
df = pd.DataFrame(data)

#create a pivot table
pivot_table = (df.pivot_table
            (values='salary',index='city',columns='age',aggfunc='mean'))
print(pivot_table)