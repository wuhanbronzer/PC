import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
data = pd.read_excel('C://users/jason/desktop/001.xls')
x = data['纬度']
y = data['经度']

plt.scatter(x, y)
plt.show()

