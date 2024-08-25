# add a new colum


import pandas as pd

#create a DataFrame
data = {
    'name':['alice','bob','charlie','david','eva']
    'age':[24,27,22,32,29]
    'city':['new york','los angles','chicogo','houstan','phonex']

}
df = pd.DataFrame(data)
#add a new column

df['salary'] = [5000,5410,1523,56300,45500,3440]
print(df)