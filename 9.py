import pandas as pd

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}
#load data into a DataFrame object :
df = pd.DataFrame(data)

print(df.loc[[0,1]])

#note :when using [],the result is a pandas DataFrame.