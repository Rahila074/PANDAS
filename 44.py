# grouping and aggregation

import pandas as pd

#create a dataframe

data = {
    'name':['alice','bob','charlie','david','eva'],
    'age':[24,27,22,32,29],
    'city':['new york','los angles','chicago','houstan','phonix'],
    'salary':[50000,60000,55000,65000,70000]
}

df = pd.DataFrame(data)

#group by city and calculate mean age and salary
grouped = df.groupby('city').agg({'age':'mean','salary':'mean'})
print(grouped)