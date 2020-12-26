# Poker Game 15点
'''from random import randint
class Poker:
    def __init__(self):
        self.num = 10
        self.member = [x for x in range(1,11)]
    def get_card(self):
        a = randint(1,self.num)
        self.num -= 1
        self.member.pop(a-1)
        return a
    @property
    def show_father(self):
        return self.num
class Player(Poker):
    def __init__(self):
        self.points = 0
    def get_card(self, point):
        self.points += point
    def check_status(self):
        return True if self.points <= 15 else False
    def show_points(self):
        return self.points
def main():
    Poke = Poker()
    Play = Player()
    Play2 = Player()
    input('start game with press 1')
    conti = False
    while not conti:
        Play.get_card(Poke.get_card())
        print(f'你当前点数是{Play.show_points()}')
        if not Play.check_status():
            print('you lose')
            print('you boomed')
            break
        Play2.get_card(Poke.get_card())
        if not Play2.check_status():
            print('you win')
            print('he boomed')
            break
        judge = input('是否继续抽牌（输入任意键继续）')
        if not judge:
            conti = True
            if Play.show_points() > Play2.show_points():
                print(f'你赢了，你的点数为{Play.show_points()}，对手的点数为{Play2.show_points()}')
            elif Play.show_points() < Play2.show_points():
                print(f'你输了，你的点数为{Play.show_points()}，对手的点数为{Play2.show_points()}')
            else:
                print('平局')


main()'''
'''from abc import ABCMeta


class MetaClass(metaclass=ABCMeta):
    def __init__(self, name, goals):
        self.name = name
        self.goals = goals

    def show_info(self):
        print(self.name, self.goals)
        return 1


class CombClass:
    def __init__(self, age):
        self.age = age

    def show_info2(self):
        print(f'this is the second class: {self.age}')


class Class1(MetaClass, CombClass):
    def show_info1(self):
        return self.name, self.goals



abc = Class1(1, 2)
print(abc.show_info())
print('--------------')
print(abc.show_info2())
print('--------------')
print(abc.name, abc.goals)'''
#09 20
'''target = []
def descending(lis):
    source_data = list(lis)
    target.append(max(source_data))
    source_data.remove(max(source_data))
    if source_data:
        descending(source_data)
    return target


a = [1,6,22,4,7,3,552,222,33,91]

print(descending(a))'''
#09 21
'''ranks = [str(n) for n in range(2,11)]+list('JQKA')
listq = list('this is')
print(listq)
'''
#10 05
#10 09
#选择排序
'''def selectionSort(alist):
      for i in range(len(alist)):
          temp = alist[i]
          for k in range(i+1, len(alist)):
              if alist[i] > alist[k]:
                  alist[i] = alist[k]
                  alist[k] = temp
                  temp = alist[i]
      return alist

def bubbleSort(alist):
    longs = len(alist)
    for _ in range(0, longs):
        s = 0
        while s < longs-1:
            if alist[s] > alist[s+1]:
                temp = alist[s]
                alist[s] = alist[s+1]
                alist[s+1] = temp
            s += 1
        longs -= 1
    return alist

def insertSort(alist):

a = [1,23,41,11,2,4,5,77,231,9,65]
print(bubbleSort(a))
'''
#10 10
#排序算法练习
#选择排序
'''import random
a = [random.randint(1,501) for _ in range(20)]
print('初始数组：' + '\n' + str(a))

def selectionSort(alist):
    for i in range(len(alist)-1):
        temp = alist[i]
        tempid = i
        for k in range(i+1, len(alist)):
            if alist[k] < temp:
                temp = alist[k]
                tempid = k
        alist[tempid] = alist[i]
        alist[i] = temp
    return alist

def bubbleSort(alist):
      longs = len(alist)
      while longs > 1:
          for i in range(0, longs-1):
              if alist[i+1] < alist[i]:
                  temp = alist[i]
                  alist[i] = alist[i+1]
                  alist[i+1] = temp
          longs -= 1
      return alist

def insrtitionSort(alist):
    for i in range(1, len(alist)):
        currentval = alist[i]
        for k in range(0, i):
            if alist[k] > currentval:
                alist.pop(i)
                alist.insert(k, currentval)
                break
    return alist

def insertition(alist):
    for index in range(1, len(alist)):
        currentval = alist[index]
        poi = index
        while poi > 0 and alist[poi-1] > currentval:
            alist[poi] = alist[poi-1]
            poi -= 1
        alist[poi] = currentval
    return alist

def quickSort(alist):
    temp = alist[0]
    left = 0
    right = len(alist)
    while left < right:
        if alist[left] > temp:
            alist[left], alist[right] = alist[right], alist[left]
            left += 1
        elif alist[right] < temp:
            alist[left], alist[right] = alist[right], alist[left]
            right -= 1

'''
# print('正确结果：'+'\n'+str(sorted(a)))
# print('排序结果：'+'\n'+str(insertition(a)))
# print(str(sorted(a)) == str(insertition(a)))
# print('------')
# print(insrtitionSort(a))

#10 15
a = 1
b = 2
print(a and b == 2)


