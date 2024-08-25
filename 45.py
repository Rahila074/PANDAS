#sorting data

import pandas as pd

#create a Dataframe

data = {
    'name':['alice','bob','charlie','david','eva'],
    'age':[24,27,22,32,29],
    'city':['new york','los angles','chicago','houstan','phonix'],
    'salary':[50000,60000,55000,65000,70000]
}

df = pd.DataFrame(data)
#sort by age

sorted_df = df.sort_values(by='age')
print(sorted_df)

#sort by multiple columns
sorted_df_multi = df.sort_values(by=['age','salary'])
print(sorted_df_multi)








