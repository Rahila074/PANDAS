#key/value objects as series
import pandas as pd

#you can also use a key/value object,

#like  a dictionery,when creating a series.

#create a simple pandas  as pd

calories = {"day1":420,"day2":380,"day3":390}

myvar = pd.Series(calories)

print(myvar)