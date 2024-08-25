#Replace only for specified columns
#The example above replaces all empty cells in the whole Data frame
#to only replace empty value for one column,
#specify the column name for one column,
#Replace null values in the "calories" column with the number 130:

import pandas as pd
df = pd.read_csv("data.csv")
df["Calories"].fillna(130,inplace=True)
print(df.to_string())