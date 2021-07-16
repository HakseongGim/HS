import pandas as pd
from datetime import datetime, timedelta

# from pandas.compact import StrinIO
API_key = 'xrJZ8HroohTzA4twNYzuzANO61JIKQYz2ZIFgnzW'

url = 'http://redash.nearthlab.com/api/queries/25/results.csv?api_key={}'.format(API_key)

df = pd.read_csv(url)

WT_name = df.loc[:, 'name']


#-----------------------------------------------------------------------------
name_Start = []
name_End = []

Start = 0
End = len(WT_name)-1

for p1, p2, i in zip(WT_name, WT_name[1:], range(len(WT_name))):
    if p1 != p2:
        name_Start.append(i)
        name_End.append(i+1)

name_Start.insert(0, Start)        
name_End.insert(len(name_End), End)

print(name_Start)
print(name_End)
