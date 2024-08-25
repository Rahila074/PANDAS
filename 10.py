#named indexes
#with the index argument, you can name your own indexes.
import pandas as pd

#add a list of name to give each row a name?

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]

}

df = pd.DataFrame(data,index = ["day1","day2","day3"])
print(df)