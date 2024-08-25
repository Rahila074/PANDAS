import numpy as np
import pandas as pd
a=pd.read_csv("C:/Users/Alisia Phini/Desktop/sample4.txt",header=None)
a.columns=['id','fname','lname','age','phn_no','loc']
print(a)

#there are 5 evaluating functions
#1.count           3.min
#2.max             4.sum         5.average

#count-oro columnthinum corresponding count kand pidikkuva

b=a.groupby('loc') ['loc'].count()
print(b)





