#ther is also tail() method
# for viewing the last rows of the DataFrame.

#the tail() method returns the headers and a specified number of rows,
#starting from the bottom.

#print thr last 5 rows of the DataFrame ?

import pandas as pd

df = pd.read_csv('data.csv')

print(df.tail()