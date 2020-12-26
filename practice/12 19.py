
# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd.read_excel(r'C:\Users\jason\Desktop\python file\《Python数据分析与挖掘实战（第2版）》源数据和代码\Python数据分析与挖掘实战（第2版）\chapter3\demo\data\dish_sale.xls')
# plt.figure(figsize=(8,4))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(data['月份'], data['A部门'], color='green', label='A部门', marker='o')
# plt.plot(data['月份'], data['B部门'], color='red', label='B部门', marker='s')
# plt.plot(data['月份'], data['C部门'], color='skyblue', label='C部门', marker='x')
# plt.legend()
# plt.ylabel('销售额（万元）')
# plt.show()
#
# #B部门各年份横向对比
# data = pd.read_excel(r'C:\Users\jason\Desktop\python file\《Python数据分析与挖掘实战（第2版）》源数据和代码\Python数据分析与挖掘实战（第2版）\chapter3\demo\data\dish_sale_b.xls')
# plt.figure(figsize=(8,4))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(data['月份'], data['2012年'], color='green', label='2012年', marker='o')
# plt.plot(data['月份'], data['2013年'], color='red', label='2013年', marker='s')
# plt.plot(data['月份'], data['2014年'], color='skyblue', label='2014年', marker='x')
# plt.legend()
# plt.ylabel('销售额（万元）')
# plt.show()


# import pandas as pd
#
# catering_sale = r'C:\Users\jason\Desktop\python file\《Python数据分析与挖掘实战（第2版）》源数据和代码\Python数据分析与挖掘实战（第2版）\chapter3\demo\data\catering_sale.xls'
# data = pd.read_excel(catering_sale)
#
# data = data[(data['销量'] > 400)&(data['销量'] < 5000)]
# statistics = data.describe()
#
# statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
# statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']
# statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']
#
# print(statistics)

# import pandas as pd
# import matplotlib.pyplot as plt
#
# df_normal = pd.read_csv(r'C:\Users\jason\Desktop\python file\dataA2\dataA2\chapter3\demo\data\user.csv')
# plt.figure(figsize=(8,4))
# plt.plot(df_normal['Date'], df_normal['Eletricity'])
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.xlabel('日期')
#
# x_major_locator = plt.MultipleLocator(7)
# ax = plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.ylabel('每日用电')
# plt.title('正常用户用电趋势')
# plt.show()
#
# #窃电用户
# df_steal = pd.read_csv(r'C:\Users\jason\Desktop\python file\dataA2\dataA2\chapter3\demo\data\Steal user.csv')
# plt.figure(figsize=(10,4))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(df_steal['Date'], df_steal['Eletricity'])
# plt.xlabel('日期')
#
# x_major_locator = plt.MultipleLocator(7)
# ax = plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.ylabel('每日用电')
# plt.title('窃电用户用电趋势')
# plt.show()

#帕累托效应
import pandas as pd

dish_profit = r'C:\Users\jason\Desktop\python file\dataA2\dataA2\chapter3\demo\data\catering_dish_profit.xls'
data = pd.read_excel(dish_profit)
data = data['盈利'].copy()
data.sort_values(ascending=False)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
data.plot()
plt.ylabel('盈利（元）')
p = 1.0*data.cumsum()/data.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
plt.ylabel('盈利（比例）')
plt.show()