#Replace using mean,median, or mode
#Replace using mean.
#Mean = the average value
##=(the sum of all value divided by number of values).
#calculate the Mean, and replace any empty of values with it ?

import pandas as pd
df = pd.read_csv('data1.csv')
x = df['Calories'].mean()
df["Calories"].fillna(x,inplace=True)
print(df.to_string())