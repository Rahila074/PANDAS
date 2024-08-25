#pandas - analysis DataFrames

#viewing the Data
#the head() method return the headers and a specified number of rows,
#starting from the top.

#print the first 10 rows and headers of csv file as DataFrame ?

import pandas as pd

df = pd.read_csv('data.csv')
print(df.head(10))