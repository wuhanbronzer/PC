import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
data = pd.read_csv("C:/users/jason/desktop/data/3.csv",parse_dates=['tdrtime'])
# print(data)
# print(np.unique(data['devic_number']))
d1 = data.copy()[(data['devic_number']==18583393017)&(data['day_id']==18)]
d1.dropna(inplace=True)
d1.sort_values(by='tdrtime', ascending=True, inplace=True)
d1.drop(axis=1, columns='data_no', inplace=True)
tdrdata = d1.copy()['tdrtime']
li= []
a = datetime.datetime(2019,12,18,16,2,31)
for i in tdrdata:
    if a > i:
        li.append((a-i).seconds)
    else:
        li.append((i-a).seconds)
nl = sorted(li)
yl = [100*(1/len(nl))*i for i in range(1,len(nl)+1)]
plt.plot(nl,yl)
plt.xlim([0,10000])
plt.show()
plt.savefig("C:/users/jason/desktop/18.jpg",ppi=200*200)
