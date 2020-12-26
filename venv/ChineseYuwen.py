from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from lxml import etree

def get_paper_name(rel_url):
    url = 'http://59.69.102.9/zgyw/index.aspx'
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    acc = browser.find_element_by_xpath('//input[@placeholder = "账号"]')
    acc.clear()
    acc.send_keys('0121702960822')
    pas = browser.find_element_by_xpath('//input[@placeholder = "密码"]')
    pas.clear()
    pas.send_keys('0121702960822')
    pas.send_keys(Keys.RETURN)
    time.sleep(1)

    browser.get(rel_url)
    names = [x.get_attribute('href') for x in browser.find_elements_by_xpath('//div[@style = "padding-left: 20px;"]/a')]
    # 点击下一页
    for i in range(5):
        try:
            browser.find_elements_by_xpath('a[@class="paginator"]')[-2].click()
            name1 = [x.get_attribute('href') for x in browser.find_elements_by_xpath('//div[@style = "padding-left: 20px;"]/a')]
            names.extend(name1)
        except:
            print('something error')
    browser.quit()
    return names
lis = []
with open('C:/users/jason/desktop/文.txt',encoding='utf8',newline='\n') as f:
    source = f.readlines()[0].split('http:')
    lis.extend(source)

for i in range(len(lis)):
    url = 'http:' + str(lis[i])
    print(url)
    print(get_paper_name(url))
'''browser.get('http://59.69.102.9/zgyw/study/LearningIndex.aspx')
titles = browser.find_elements_by_xpath('//div[@class = "h2_cat"]/a')
rel_titles = [k.text for k in titles]
for i in range(len(rel_titles)):
    with open(f'C:/users/jason/desktop/{rel_titles[i]}.txt','w',encoding='utf8') as f:
        times = browser.find_elements_by_xpath('//div[@class = "h3_cat"]//li//a')
        for k in times:
            f.write(k.get_attribute('href'))'''

'''
#开始学习
browser.get('http://59.69.102.9/zgyw/study/LearningIndex.aspx')
urlList = []
lis = browser.find_elements_by_xpath('//li/a')
for i in range(7,39):
    driver = webdriver.Chrome()
    new_url = str(lis[i].get_attribute('href'))
    driver.get(new_url)
    time.sleep(1)
    lis1 = driver.find_elements_by_xpath('//div[@class = "ll_title"]//a')
    for k in range(0,len(lis1)):
        new1_url = str(lis1[k].get_attribute('href'))
        urlList.append(new1_url)
    driver.close()
with open('C:/users/jason/urls.txt','w',encoding='utf8') as f:
    for i in urlList:
        f.write(str(i)+'\n')
print("完成")'''
'''print(new_url)
        browser.get(new1_url)
        time.sleep(15)
        js = "var q=document.documentElement.scrollTop=1000"
        browser.execute_script(js)
        browser.close()
'''
'''from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://59.69.102.9/zgyw/study/LearningIndex.aspx')
urlList = []
lis = browser.find_elements_by_xpath('//li/a')
for i in range(7,39):
    new_url = str(lis[i].get_attribute('href'))
    js = f'window.open("{new_url}")'
    browser.execute_script(js)
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])
    time.sleep(5)
'''