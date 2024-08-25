#locate named indexes
#use the named index in the loc attribute to return the specified row(s).

#return "day2" ?

import pandas as pd
data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data,index = ["day1","day2","day3"])

print(df.loc["day2"]) #return series

#use the named index in the loc attribute to return row 1 and row 2?
print(df.loc[["day1","day2"]])#return DataFrame