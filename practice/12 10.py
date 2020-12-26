'''from scipy.optimize import fsolve
def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]
result = fsolve(f, [1,1])
print(result)'''
'''from scipy import integrate
def g(x):
    return (1-x**2)**0.5
pi_2, err = integrate.quad(g, -1, 1)
print(pi_2*2)'''
'''import pandas as pd
catering_sales = 
data = pd.read_excel(catering_sales, index_col='日期')

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
p = data.boxplot(return_type='dict')
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy = (x[i], y[i]), xytext=(x[i]+0.05 - 0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy = (x[i], y[i]), xytext=(x[i]+0.08, y[i]))
plt.show()'''
import pandas as pd
import numpy as np
catering_sale = r'C:\Users\jason\Desktop\PythonData\PythonData\chapter3\demo\data\catering_fish_congee.xls'
data = pd.read_excel(catering_sale, names=['date', 'sale'])
bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
labels = ['[0, 500)', '[500, 1000)', '[1000, 1500)', '[1500, 2000)', '[2000, 2500)', '[2500, 3000)', '[3000, 3500)', '[3500, 4000)']
data['sale分层'] = pd.cut(data.sale, bins, labels=labels)
aggResult = data.groupby('sale分层')['sale'].agg('sale': np.size)
pAggResult = round(aggResult/aggResult.sum(), 2, )*100
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
pAggResult['sale'].plot(kind='bar', width=0.8, fontsize=10)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('季度销售额频率分布直方图', fontsize=20)
plt.show()