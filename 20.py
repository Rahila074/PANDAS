#pandas read json

import pandas as pd

df = pd.read_json('jhai.json')

print(df.to_string())

#tip:use to string () to print the entire Dataframe