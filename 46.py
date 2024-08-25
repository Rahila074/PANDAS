#merging data frame

import pandas as pd

#create two Data frame
data1 = {
    'name':['alice','bob','charlie'],
    'age':[24,27,22]

}

df1 = pd.DataFrame(data1)

data2 = {
    'name':['alice','bob','david'],
    'city':['new york','los angles','houstan']

}

df2 = pd.DataFrame(data2)

#merge Dataframes on 'name'

merged_df = pd.merge(df1,df2, on='name',how='inner')
print(merged_df)