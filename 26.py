#replace empty values
#Another way of deadline with empty cells is to insert a new value instead.
#This way you do not have to delete entire rows just
#because of some empty cells.
#the fillna() method allows us to replace empty cells with a value ?

#replace null values with the number 130 ?
import pandas as pd

df= pd.read_csv("data1.csv")
df.fillna(130,inplace=True)
print(df.to_string())