'''import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests'''
# browser = webdriver.Chrome()
# try:
#     source = browser.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
#     WebDriverWait(source, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"content"),'通关'))
#     print(browser.page_source)
# except Exception as _:
#     print('网页加载太慢，不等了')
'''browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.591b23e1bcXF1d&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=')
time.sleep(5)
elements = browser.find_elements_by_xpath('//div[@class = \'items__txt__title\']/a')
for a in elements:
    print(a.text)'''
'''source = requests.get('http://fund.eastmoney.com/pingzhongdata/005983.js?v=20200909162915')
print(source)
print(source.text)
'''
#模拟登录
'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://accounts.douban.com/passport/login')
driver.find_element_by_xpath('//li[@class = "account-tab-account"]').click()
elem = driver.find_element_by_xpath('//input[@name = "username"]')
elem.clear()
elem.send_keys('18186451692')
passw = driver.find_element_by_xpath('//input[@id = "password"]')
passw.clear()
passw.send_keys('1122335Wang')
input('请输入验证码')
passw.send_keys(Keys.RETURN)
time.sleep(10)
print(driver.page_source)'''
#使用cookies
'''import requests
headers = {
    'Cookie':'_zap=eb72232f-d2d2-4efa-98ab-69b15419e715; _xsrf=elHMilZDPAwQMKnrrSZczIud7BfSaCXc; d_c0="AABj8TKs_g-PTi50A6uthPjtfZSevTnqMEc=|1567568830"; __utma=51854390.876274011.1575770774.1575770774.1575770774.1; __utmv=51854390.100--|2=registration_date=20171127=1^3=entry_date=20171127=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1575465122,1575770398,1576462983,1576985952; q_c1=d0317e7693e94e9fa7e32cd727c9feb7|1578738530000|1575770769000; tst=r; SESSIONID=uj9SDaD1Zwro367v85L7runy7Ysd4VIKbUlYSzcFzfm; JOID=V1kVAEIa8WKlbcQLcRwpMoavktVla5pY_CWhTkNMghHJVP44BoVKM_xlwQl4uHr0d1EYx4IyzFqFnhzp66NM8Ao=; osd=VVoWCk8Y8mGvYMYIchYkMIWsmNhnaJlS8SeiTUlBgBLKXvM6BYZAPv5mwgN1unn3fVwaxIE4wViGnRbk6aBP-gc=; capsion_ticket="2|1:0|10:1599650203|14:capsion_ticket|44:NDMzOWM0MWYzNTY2NDRkYTk1ZGIyMzA2ZWExNGE2ZmY=|c6375f7ce9dfa3cd5f65d5535bd7182ad7c5bfef6d8d19008b0f579e6ae77eeb"; z_c0="2|1:0|10:1599650209|4:z_c0|92:Mi4xZHQtcUJnQUFBQUFBQUdQeE1xei1EeVlBQUFCZ0FsVk5vUWRHWUFDeVhOZlc4NGZNS3BzLTBNZFJiMm4zWGVsTzhn|8ee7d57cf9458a1bb706573c657989edfc06da883b589627c55eb5ca1b45783a"; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1599650235|1599650201',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
session = requests.Session()#保存对话ID，使访问行为更加类人化
browser = session.get('https://www.zhihu.com',headers=headers, verify=False)
browser.encoding = 'utf8'
with open('C:/users/jason/desktop/spider.txt','w',encoding='utf8') as f:
    f.write(browser.text)
'''
#使用表单登录
'''import requests
login_url = 'http://exercise.kingname.info/exercise_login'
login_success_url = 'http://exercise.kingname.info/exercise_login_success'

data = {
    'username':'kingname',
    'password':'genius',
    'remember':'Yes'
}

session = requests.Session()
before_login = session.get(login_success_url).text
print(before_login)
print('=====开始登录=====')
session.post(login_url,data=data).text#登录成功后，cookie会被保存在session中
after_login = session.get(login_success_url).text
print(after_login)'''
#验证码
