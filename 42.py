#pandas - removing duplicates
#the duplicates () method returns a boolean values for each rows:

#return true for every row that is a duplicates, otherwise False/

import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())