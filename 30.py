#Calculate the MODE, and replace any empty value with  it?

#mode = the value that appears most frequently .

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df['Calories'].fillna(x,inplace=True)
print(df.to_string())