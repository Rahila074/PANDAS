#DataFrames
#Data sets in pandas are usually multi-dimensional tables,
#called DataFrames
#series is like a column, a DataFrame is the whole table.

#create a DataFrame from two series ?

import pandas as pd

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]

}

myvar = pd.DataFrame(data)

print(myvar)