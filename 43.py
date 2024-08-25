#removing duplicates

#to remove duplicate ,
#use the drop_duplicates () method.

#remove all duplicates ?

import pandas as pd

df = pd.read_csv('data1.csv')
df.drop_duplicates(inplace=True)

print(df.to_string())