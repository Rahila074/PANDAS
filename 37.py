#pandas - cleaning Data of wrong format
#data of wrong format
#cells with data of wrong format can make it difficult,
#or even impossible, to analyse data.

#to fix it , you have two options :
#remove the rows , or
#convert all cells in the column into same formmat.

#pandas has to datetime() method for this:

import pandas as pd
df = pd.read_csv('dd.csv')
df['Date']= pd.to_datetime(df['Date'])

print(df.to_string())