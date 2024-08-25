#create lables

#with the index arguments, you can name your own lables.

#create your own lables?

import pandas as pd

a = [1,7,2]

myvar = pd.Series(a, index = ["x","y","z"])

print(myvar)

#return the value of "y"?

print(myvar["y"])