import requests
from lxml import etree
url = 'http://www.eqiutan.cn/p/c/418/clubtransferin_1.html'
for i in range(1,20):
    source = requests.get(f'http://www.eqiutan.cn/p/c/418/clubtransferin_{i}.html')
    print(f'第{i}页状态码为{source}')
    source.encoding = 'utf8'
    raw_data = etree.HTML(source.text)
    lines = raw_data.xpath('//div[@class="tsfrcd"]//tr//li//a')
    with open('C://users/jason/desktop/Real.txt', 'a+', encoding='utf8') as f:
        for i in lines:
            f.write(i.text + "\n")