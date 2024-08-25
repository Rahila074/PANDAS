#load files into a Dataframe

#if your data sets are stored in aa dile,
#pandas can load them into a DataFrame .

#load a comma separeted file (csv file ) into a Dataframe

import pandas as pd

df = pd.read_csv("data.csv")

print(df)