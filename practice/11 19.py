'''import requests
import re
from lxml import etree
data = {
    'username' : '18186451692',
    'password': '22590JasonK',
    'captcha':'1111'
}
url1 = 'https://account.guokr.com/sign_in/?success=http%3A%2F%2Faccount.guokr.com%2Foauth2%2Fauthorize%2F%3Fclient_id%3D32353%26redirect_uri%3Dhttp%253A%252F%252Fwww.guokr.com%252Fsso%252F%253Flazy%253Dy%2526rid%253D4071656635%2526success%253Dhttps%25253A%25252F%25252Fwww.guokr.com%25252F%26response_type%3Dcode%26state%3Dfebaa2ce7dee893fdab4b31777b98d83330ea98599236ed8b4a8d51dd6804b76--1605794082%26suppress_prompt%3D1'
source = requests.post(url1, data=data)
print(source)
print('--------------')
with open('C://users/jason/desktop/1.jpg', 'wb') as f:
    f.write(source.content)
ea = etree.HTML(source.text)
str = ea.xpath('//body//div//p[@style="white-space: normal;"]')
print(len(str))
with open('C://users/jason/desktop/text.txt', 'w', encoding='utf8') as f:
    for i in str:
        if i.text != None:
            f.write(i.text + '\n')'''
a = '你'
b = a.encode('utf8')
c = ord('你')
print(c)
print(b)