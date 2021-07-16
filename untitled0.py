import pandas as pd
from datetime import datetime, timedelta

# from pandas.compact import StrinIO
API_key = 'xrJZ8HroohTzA4twNYzuzANO61JIKQYz2ZIFgnzW'

url = 'http://redash.nearthlab.com/api/queries/25/results.csv?api_key={}'.format(API_key)

df = pd.read_csv(url)

WT_name = df.loc[1, 'name']
WT_number = df.loc[:, 'title']

Date_str = df.loc[:, 'yymmdd'] 
Time_str = df.loc[:, 'hhmmss']

#-----------------------------------------------------------------------------
Time = []
for i in range(len(WT_number)):
    elm = datetime.strptime(Time_str[i], '%H:%M:%S') + timedelta(hours=9)   
    Time.append(elm.time())

Time = pd.Series(Time)

# >>> today.isoformat()                    # ISO 표준 문자열 표현
# '2017-11-14'

#-----------------------------------------------------------------------------
number_Start = []
number_End = []

Start = 0
End = len(WT_number)-1

for p1, p2, i in zip(WT_number, WT_number[1:], range(len(WT_number))):
    if p1 != p2:
        number_Start.append(i+1)
        number_End.append(i-5)

number_Start.insert(0, Start)        
number_End.insert(len(number_End), End)
#-----------------------------------------------------------------------------

Time_interval = []

for p1, p2 in zip(number_Start, number_End):
    # elm = datetime.strptime(Time_str[p2],'%H:%M:%S') - datetime.strptime(Time_str[p1],'%H:%M:%S')
    elm = datetime.strptime(Time_str[p2],'%H:%M:%S') - datetime.strptime(Time_str[p1],'%H:%M:%S')

    Time_interval.append(elm)
    
total_data = pd.DataFrame(zip(WT_number[number_Start], Time[number_Start], Time[number_End], Time_interval))
total_data.columns = ['호기','시작시간','종료시간','점검시간']

#-----------------------------------------------------------------------------
folder = 'WT_inspection'
save_name = '점검시간.csv'

# total_data.to_csv('C:\\Users\\HakSeong Gim\\Desktop\\{}/{}'.format(folder, save_name), encoding = 'utf-8-sig', index=False)

