import numpy as np
import pandas as pd
a=pd.read_csv("C:/Users/Alisia Phini/Desktop/Temperature",header=None,sep=" ")
a.columns=['year','temp']

#syntax
#newdfname=olddfname.groupby('columnname') ['columnname'].max()
b=a.groupby('year') ['temp'].max().sort_values(ascending=False)
print(b)






