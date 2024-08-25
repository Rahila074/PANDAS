#info about the data

#the DataFrames object has a method called info()
#that gives you more information about the data set.

#print information about the data?

import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())