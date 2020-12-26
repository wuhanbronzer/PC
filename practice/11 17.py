import re
with open('C:/users/jason/desktop/1.txt','r',encoding='utf8') as f:
    source = f.read()
UID = re.findall('//space.bilibili.com/(.*?)/\"', source)
with open('C:/users/jason/desktop/UID1.txt', 'w', encoding='utf8') as f:
    for i in range(len(UID)):
        if i%2 == 0:
            f.write(UID[i] + '\n')