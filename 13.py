import pandas as pd

#create a dataframe

data ={
    'name':['alice','bob','charlie','david','eva'],
    'age':[24,27,22,32,29],
    'city':['newyork','los angles','chicago','huston','phonix']}

df = pd.DataFrame(data)
print(df)