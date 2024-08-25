import pandas as pd
#data selection

#create a DataFrame
data = {
    'name':['alice','bob','charlie','david','eva'],
    'age':[24,27,22,32,29],
    'city':['newyork','los angles','chicago','houston','phonix']

}

df = pd.DataFrame(data)

#select a single columns
print(df[['name','age']])

#select multiple columns
print(df[['name','age']])

#select row by index
print(df.iloc[0:3])    #first three rows

#Select rows by index
print(df[df['age']>25])