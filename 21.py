#dictionery as json

#json = python dictionery

#json object have the same format ass python dictioneries

#load a python dictionery into a dataframe

import pandas as pd

data = {
    "duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "5":60

    },
    "pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
         "5":102
    },
    "maxpulse":{
        "0":409,
        "1":479,
        "2":340,
        "3":282,
        "4":406,
        "5":300
    },
}


df = pd.DataFrame(data)
print(df)