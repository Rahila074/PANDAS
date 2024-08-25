#increase the maximum number of rows to display the entire dataframe


import pandas as pd

#set display options to show maximum rows and columns

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

#load your csv file

df= pd.read_csv('big.csv')
#print the entire DataFrame
print(df.to_string())