#Pandas - fixing wrong data

#replacing values
#one way to fix wrong values is to replace them with something else

#in our example, it is most likely a typo,
#and the value should be "45" instead of "450",
#and we could just insert "45" in rows 7:
#SEt "duration" = 45 in row 1 ?

import pandas as pd

df = pd.read_csv("wrong.csv")

df.loc[1,'Duration'] = 45
print(df.to_string())