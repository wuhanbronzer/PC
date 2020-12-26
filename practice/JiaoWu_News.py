import requests
from lxml import etree
url = 'http://i.whut.edu.cn/bmxw/index.shtml'
data = requests.get(url)
data.encoding = 'utf8'
source = etree.HTML(data.text)
lis = source.xpath('//ul[@class="normal_list2"]//li//a/@title')
check_point = input('输入要查询的部门')
if check_point:
    for i in lis:
        if check_point in i:
            print(i)
else:
    for i in lis:
        print(i)

