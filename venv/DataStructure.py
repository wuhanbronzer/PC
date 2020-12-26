#无序表
#创建构建节点
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,data):
        self.data = data

    def setNext(self,newnext):
        self.next = newnext#
class UnorderedList:
    def __init__(self):
        self.head = None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self,data):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = True
        while not found:
            if current.getData() == item:
                found = False
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())
    def value(self,posi):
        count = 0
        current = self.head
        while count != posi:
            count += 1
            current = current.getNext()
        return current.getData()
    def insert(self,posi,item):
        count = 0
        temp = Node(item)
        current = self.head
        previous = None
        while count != posi:
            count += 1
            previous = current
            current = current.getNext()
        temp.setNext(current)
        previous.setNext(temp)

#有序表
class OrderrdList:
    def __init__(self):
        self.head = None

#递归
import sys
sys.setrecursionlimit()#设置递归层数
#迷宫
class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist =[]
        mazeFile = open(mazeFileName,'r')
        for line in mazeFile:
            rowlist = []
            col = 0
            for ch in line[:-1]:
                rowlist.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazelist.append(rowlist)
            columnsInMaze = len(rowlist)