#Calculate the MEDIAN , and  replace any empty valus with it?

#median = the value in the middle,
#after you have sorted all values asceding .

import pandas as pd
df = pd.read_csv('data1.csv')
x = df['Calories'].median()
df["Calories"].fillna(x,inplace=True)
print(df.to_string())