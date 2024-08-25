

import  pandas as pd

#create a DataFrame
data = {
'name':['alice','bob','charlie','david','eva'],
    'age':[24,27,22,32,29],
    'city':['newyork','los angles','chicago','houston','phonix'],
    'salary':[5000,4000,6000,9000,7000]

}
df = pd.DataFrame(data)

#delete a column

df.drop('salary',axis=1,inplace=True)
print(df)