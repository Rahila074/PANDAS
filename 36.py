import pandas as pd
import numpy as np

# handling missing data
#create a dataframe with missing values
data = {
    'name':['alice','bob','charlie','david','eva'],
    'age':[24,np.nan,22,32,29],
    'city':['new york','los angless','chicago',np.nan,'phonix']
}
df = pd.DataFrame(data)
#drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

#filling missing values
df_dropped = df.fillna({'age':df['age'].mean(),'city':'unknown'})
print(df_dropped)