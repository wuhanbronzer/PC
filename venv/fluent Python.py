'''def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

        >>> [factorial(n) for n in range(6)]
        [1, 1, 2, 6, 24, 120]
        >>> factorial(30)
        265252859812191058636308480000000
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: n must be >= 0

        Factorials of floats are OK, but the float must be an exact integer:
        >>> factorial(30.1)
        Traceback (most recent call last):
            ...
        ValueError: n must be exact integer
        >>> factorial(30.0)
        265252859812191058636308480000000

        It must also not be ridiculously large:
        >>> factorial(1e100)
        Traceback (most recent call last):
            ...
        OverflowError: n too large
        """
    import math
    if not n >=0:
        raise ValueError('n must be >= 0')
    if math.floor(n) != n:
        raise ValueError('n mus be integer')
    if n+1 == n:
        raise OverflowError('n too large')
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testfile('simple.txt')'''
#dunder-method
'''import collections
Card = collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split( )
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
'''
'''# beer_card = Card('7', 'diamonds')
# print(beer_card)
# deck = FrenchDeck()
# print(deck.__len__())
# print(deck[6])
# print('-----------')
# from random import choice
# print(choice(deck))
#print(deck[12::13])#找出所有A卡
'''
#反向迭代
'''for card in reversed(deck):
    print(card)
'''
#排序：2最小，A最大
'''suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]#这里必须先乘上len()，否则排序时会造成相邻的花色乱序
for card in sorted(deck, key=spades_high):
    print(card)'''
#用特殊方法模拟数值类型
#模拟向量
'''from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    #return bool(self.x or self.y) 另一种高效写法，无需计算模
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y *scalar)

a = Vector()
print(a)'''
#列表推导式推导笛卡尔积
'''colors = ['black', 'white']
sizes = ['S','M','L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)'''
#使用生成器进行for循环节省内存开销。因为生成器在每次运行时才会产生组合，原来的组合不会保存在内存里
'''colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s%s'%(c, s) for c in colors for s in sizes):
    print(tshirt)'''
#嵌套元组获取经纬度（格式化输出）
'''metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR','IN', 21.935,(28.613889, 139.691667))
]
print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))'''
#具名元组
'''from collections import namedtuple
City = namedtuple('City', 'name country population corrdinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139,691667))
print(tokyo.population)'''
#切片
"""invoice = '''
0.....6..........40........52...55......
1909 Pimoroni PiBrella     $17.5   3   $52.50
1489 6mm Tactile Switch x20   $4.95  2  $9.90
1510 Panavise Jr. -PV-201     $28.00  1  $28.00
1601 PiTFT Mini Kit 320x240   $34.95  1  $34.95'''
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])"""
#切片的赋值及修改
'''l = list(range(10))
l[2:5] = [20,30]
del l[5:7]
l[3:2] = [11, 22]'''
#bisect查找元素插入位置（升序排列）
'''import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 24, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))
if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack->', ' '.join('%2d'%n for n in HAYSTACK))
    demo(bisect_fn)
'''
#bisect成绩分类
'''import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
li = [grade(score) for score in [39,99,77,70,89,90]]
print(li)'''
#使用bisect.insort将元素插入有序序列
'''import bisect
import random
SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d->'%new_item, my_list)
'''
#数组创建、存取过程
'''import time
from array import array
from random import random
start = time.time()
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
end = time.time()
print(floats2[-1])
print(floats == floats2)
print(f'花费{end-start}秒')'''
#通过改变数组中的一个字节来更新数组里某个元素的值
'''import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct)
memv_oct.tolist()
memv_oct[5] = 4
print(numbers)'''
#初探numpy
'''import numpy
floats = nunmpy.loadtxt('floats-10M-lines.txt')
from time import perf_counter as pc #高精度 高性能计时
t0 = pc()
floats /= 3
print(pc() - t0)
numpy.save('floats-10M', floats)
floats2 = numpy.load('floats-10M.npy', 'r+')'''
#字典构造式
'''DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
print('----------')
print({code:country.upper() for country, code in country_code.items() if code < 66})'''
#使用UserDict创建Dict实例
'''import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.data
    def __setitem__(self, key, value):
        self.data[str(key)] = item
'''
#集合交集操作
'''haystack = (1,2,3)
needles = (2,3)
found = len(needles & haystack)
found1 = len(set(needles).intersection(haystack))'''
#编码相关
#
'''from unicodedata import normalize, name
ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))'''
#去掉变音符号
'''import unicodedata
import string
def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    #过滤掉组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)
#去掉拉丁文的变音符号字符
def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
        shaved = ''.join(keepers)
        return unicodedata.normalize('NFC', shaved)'''
#用户定义的可调用类型
'''import random
class BingoCage:
    def __init__(self, items):
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()'''
#生成HTML标签
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s"'%(attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>'%(name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />'%(name, attr_str)