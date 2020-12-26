#寻找水仙花数：一个三位数，每个数位上的立方之和等于该数本身
'''for i in range(100,1000):
    digit = i % 10
    decade = (i % 100)//10
    hundreds = i //100
    if (digit**3 + decade**3 + hundreds**3) == i :
        print(f"{i}是一个水仙花数")'''
#正整数反转
'''lis = []
def mods(num):
    los = num % 10
    num = num // 10
    lis.append(los)
    fina = 0
    if num >= 10 :
        mods(num)
    else:
        lis.append(num)
    for i in range(1,len(lis)+1):
        fina = fina + lis[i-1]*(10**(len(lis)-i))
    return fina
intt = int(input('请输入一个正整数'))
print(mods(intt))'''
'''num = int(input('num = '))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num*10 + num%10
    num //= 10
print(reverse_num)#妙啊'''
#Craps赌博游戏
'''import random
money = 1000
for i in range(100):
    input('输入1开始游戏')
    while True:
        debt = int(input(f'请下注(金额为整)|当前余额{money}'))
        if 0 < debt <= money:
            break
    num1 = random.randint(1,7) + random.randint(1,7)#应该加入更换随机数种子！！！
    go_on = False
    if num1 == 1 or 7:
        print('玩家胜')
        money += debt
    elif num1 == 2 or 3 or 12:
        print('庄家胜')
        money -= debt
    else:
        go_on = True
    while go_on:
        go_on = False
        num2 = random.randint(1,7) + random.randint(1,7)
        if num2 == num1:
            print('玩家胜')
            money += debt
        elif num2 == 7:
            print('庄家胜')
            money -= debt
        else:
            go_on = True
    print(f'剩余赌资{money}')
'''
#生成斐波那契shulie
'''li = [1,1]
for i in range(2,21):
    new_num = li[i-2] + li[i-1]
    li.append(new_num)
print(li)'''
#函数变量作用域
'''def f00():
    b = 'hello'
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar()
if __name__ == '__main__' :
    a = 100
    f00()'''
#生成式与生成器
'''import sys
import time
f = [x**2 for x in range(1000)]#列表生成表达式，创建列表之后，元素就已经准备就绪，耗费内存较多
print(sys.getsizeof(f))
a = (x**2 for x in range(1000))#创建一个生成器对象
print(sys.getsizeof(a))
for i in range(10):
    print(next(a))'''
#字典构造器
'''item1 = dict(one=1,two=2,three=3)
item2 = dict(zip(['a','b','c'],'12'))
item3 = {num: num**2 for num in range(10)}
print(item2.pop('b',55))
print(item2)'''
#跑马灯
'''import os
import time
contebt = '武汉欢迎你...'
while True:
    os.system('cls')
    print(contebt)
    contebt = contebt[1:] + contebt[0]
    time.sleep(0.2)'''
#返回指定文件后缀名
'''def get_suffix(filename, has_dot = False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos+1
        return filename[index:]
    else:
        return '''''
#返回传入列表中前二大的元素值
'''def get_big(lis):
    bigg = max(lis)
    lis.remove(bigg)
    sec = max(lis)
    return bigg,sec
li = [1,2,5,7,9,5,3,33,26,56]
print(get_big(li))'''
#面向对象编程——类
'''class Test:
    def __init__(self,foo):
        self.__foo=foo
    def bar(self):
        print(self.__foo)
        print('__bar')
test = Test('hellos')
test.bar()
print(test.__foo)#双下划线开头的属性是私有属性，需要用特殊的方法访问
'''
#数字时钟类
'''from time import sleep
class clock:
    def __init__(self,seconds,minuates,hours):
        self.minuates = minuates
        self.seconds = seconds
        self.hours = hours
    def run(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minuates += 1
        if self.minuates == 60:
            self.minuates = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
    def show(self):
        print(f'现在时{self.hours}时{self.minuates}分{self.seconds}秒')
now = clock(11,58,19)
while True:
    now.run()
    now.show()
    sleep(1)'''
#关于类对象
'''class Tool:
    count = 0
    def __init__(self,name):
        self.name = name
        Tool.count += 1
    @classmethod
    def check(cls):
        print(cls.count)
t1 = Tool('1')
t2 = Tool('2')
Tool.check()'''
#奥特曼打小怪兽
from abc import ABCMeta, abstractmethod
from random import randint, randrange
'''
class Fighter(metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self,name,hp):
        # 初始化方法
        # :param name:名字
        # :param hp:生命值
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        # 攻击
        # :param:被攻击的对象
        pass

class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp, mp):
        # 初始化方法
        # :param name:Mingzi名字
        # :param hp:生命值
        # :param mp:魔法值
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15,25)

    def huge_attack(self,other):
        # 究极必杀技（打掉对方50-3/4的血量
        # :param other
        # :return:使用成功返回True否则False
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10.15)
            return True
        else:
            return False

    def resume(self):
#恢复魔法值
        incr_point = randint(1.10)
        self._mo += incr_point
        return incr_point

    def __str__(self):
        return f'f{self._name} \n {self._hp} \n {self._mp}'

class Monster(Fighter):
    __slots__ = ('_name','_hp')

    def attack(self, other):
        other.hp -= randint(10,20)

    def __str__(self):
        return f'f{self._name} \n {self._hp}'

def is_any_alive(monsters):
    for mons in monsters:
        if mons.alive > 0:
            return True
    return False
def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for mon in monsters:
        print(mon, end='')
'''
#进程与线程
#未作多进程处理
'''from random import randint
from time import sleep, time
def download_task(filename):
    print(f'开始下载{filename}')
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f'{filename}下载完成，花费{time_to_download}秒')

def main():
    start = time()
    download_task('py1')
    download_task('py2')
    end = time()
    print(f'共计花费了{end-start}秒')

if __name__ == '__main__':
    main()
'''
#进行多进程处理
'''from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print(f'启动下载进程，进程号{getpid()}')
    print(f'开始下载{filename}')
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f'{filename}下载完成，花费{time_to_download}秒')

def main():
    start =time()
    p1 = Process(target=download_task, args=('p1', ))
    p1.start()
    p2 = Process(target=download_task, args=('p2', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'共计花费{end-start}秒')
if __name__ == '__main__':
    main()'''
#多线程工作案例
'''from time import sleep
from threading import Thread, Lock

class Account(object):
     def __init__(self):
         self._balance = 0
         self._lock = Lock()

     def deposit(self, money):
         self._lock.acquire()
         try:
             new_balance = self._balance + money
             sleep(0.01)
             self._balance = new_balance
         finally:
             self._lock.release()

     @property
     def balance(self):
         return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()#了解super的用法
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)#这个deposit方法是怎么继承过来的？

def main():
    accounts = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(f'账户余额为：{accounts.balance}')
'''
#多线程应用案例2
'''import time
import tkinter
import tkinter.messagebox

def download():
    time.sleep(10)
    tkinter.messagebox('提示','下载完成')

def show_about():
    tkinter.messagebox.showinfo('关于','作者：jackfrued')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost',True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()
'''
#多线程应用案例——员工工资结算系统
'''from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta:'''
#生成式推导
'''prices = {
    'AApl':191.88,
    'GOOG':1186.9,
    'IBM':149.24,
    'ORCL':48.44,
    'ACN':166.89,
    'FB':208.9,
    'SYMC':21.29
}
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)'''
#嵌套列表
'''import random
names = ['关羽','张飞','赵云','马超','黄忠']
courses = ['语文','数学','英语']
scores = [[None] * len(courses) for _ in range(len(names))]
print(f'scores内的内容是：{scores}')
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(random.randint(1,101))
print(scores)'''
#headq模块（堆排序）
'''import heapq
list1 = [34,25,12,99,87,63,58,88,92]
list2 = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL','shares':50,'price':543.22},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45,'price':16.35},
    {'name':'ACME','shares':75,'price':115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(2, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
'''
#itertools模块
'''import itertools
#产生ABCD的全排列
itertools.permutations('ABCD')
#产生ABCD的５选３组合
itertools.combinations('ABCDE',3)
#产生ABCD和123的笛卡尔积
itertools.product('ABCD','123')
#产生ABC的无限循环序列
itertools.cycle(('A','B','C'))'''
#排序算法
#简单选择排序
'''def select_sort(items, comp=lambda x,y: x<y):
    items = items[:]#声明了items的数据类型
    for i in range(len(items) - 1):
        min_index = 1
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[j]
    return items
#冒泡排序
def bubble_sort(items, comp = lambda s, y: s > y):
    items = items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items
#搅拌排序（冒泡排序升级版）：个人理解，相当于是从前往后排一次，再从后往前排一次，直至排序完成
#对于某些数据排列可能有比较好的效率
def mash_bubble_sort(items, comp = lambda x, y: x> y):
    items = items[:]
    for i in range(len(items) - 1)
        swapped = False
        for j in range(len(items) - 1):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j -1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break
    return items'''
#百元百鸡之穷举法
'''for g in range(0,101):
    for m in range(0,101):
        for x in range(0,101):
            if g + m + x == 100 and 5*g + 3*m + x/3 == 100:
                print(f'公鸡{g}只，母鸡{m}只，小鸡{x}')
'''
#五人分鱼
'''fish =6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1)%5==0:
            total = (total - 1) // 5*4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5
'''
#贪婪算法与小偷
'''class Thing:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        #价格重量比
        return self.price / self.weight

def input_thing():
    name_str, price_str, weight_str = input().split()
    return name_str, price_str, weight_str

def main():
    max_weight, num_of_things = map(int, input().split())
    all_things =[]
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值：{total_price}美元')
if __name__ == '__main__':
    main()'''
#分治法例子——快速排序
#选择枢轴对元素进行划分，左边都比枢轴小，右边都比枢轴大
'''def quick_sort(items, comp=lambda x, y: x<=y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items

def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos-1, comp)
        _quick_sort(items, pos + 1, end , comp)

def _partition(items, start, end, comp):
    pivot = items[end]
    i = start -1
    for j in range(start, end):
        if comp(items[j],pivot):
            i += 1
            items[i],items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i+1]
    return i+1
'''
#动态规划例子——子列表元素求和
'''def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1,len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)'''
#x=6
'''count = 200
def outer():
    count = 10    # enclosing 嵌套作用域
    def inner():
        # nonlocal count  # 引用 enclosing 的 count = 10，如果不加，print(count) 会引用 enclosing 的 count = 10
        global count   # 这里引用最外层的 global 的 count = 200
        count = 20  # 修改 enclosing 的 count
        print(count)
    inner()
    print(count)  # 这里的值不是 outer 的 count ，而是 inner 的 count
outer()
print(count)'''
#面向对象编程三大方法：封装、继承、多态
#工资结算系统：部门经理每月15000、程序员每小时200、销售员1800底薪加销售额5%的提成
'''from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def get_salary(self):
        #结算月薪、抽象方法
        pass
class Manager(Employee):
    def get_salart(self):
        return 15000.0
class Programmer(Employee):
    def __init__(self,name, working_hour = 0):
        self.working_hour = working_hour
        super().__init__(name)
    def get_salary(self):
        return 200.0 * self.working_hour
class Salesman(Employee):
    def __init__(self, name, sales = 0.0):
        self.sales = sales
        super().__init__(name)
    def get_salary(self):
        return 1900.0 + self.sales * 0.05

class EmployeeFactory:
    @staticmethod
    def create(emp_type, *args, **kwargs):
        all_emp_types = {'M': Manager, 'P':Programmer, "S":Salesman}
        cls = all_emp_types[emp_type]
        return cls(*args, **kwargs) if cls else None

def main():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}:{emp.get_salart():.2f}元')
if __name__ == '__main__':
    main()'''
