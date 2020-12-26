#贪心策略
'''def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c < change]:
            numcoin = 1 + recDC(coinValueList, change-i, knownResults)
            if numcoin < minCoins:
                minCoins = numcoin
                knownResults[change] = minCoins
    return minCoins'''
#动态规划
'''def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <=cents]:
            if minCoins[cents-1] + 1 < coinCount:
                coinCount = minCoins[cents-1] + 1
            minCoins[cents] = coinCount
        return minCoins[change]'''
#无序表查找
'''def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found'''
#二分查找
'''def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] > item:
            last = midpoint-1
        elif alist[midpoint] < item:
            first = midpoint+1
    return found
'''
#冒泡排序（改良版）
'''def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1],alist[i]
            passnum -= 1'''
#选择排序
'''def selectionSort(alist):
    for fillsort in range(len(alist)-1, 0, -1):
        pos = 0
        for location in range(1, fillsort+1):
            if alist[location] > alist[pos]:
                pos = location
        temp = alist[fillsort]
        alist[fillsort] = alist[pos]
        alist[pos] = temp
    return alist
a = [1,3,2,11,55,2,32,41]
print(selectionSort(a))'''
#插入排序
'''def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        poi = index
        while poi > 0 and alist[poi-1] > currentvalue:
            alist[poi]=alist[poi-1]
            poi -= 1
        alist[poi] = currentvalue
    return alist
a = [1,55,3,2,66,85,34,11]
print(insertionSort(a))'''
#谢尔排序
'''def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startpoi in range(sublistcount):
            gapInsertionSort(alist, startpoi, sublistcount)
        print('After increments of size', sublistcount, 'The list is', alist)
        sublistcount /= 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        poi = i
        while poi >= gap and alist[poi-gap]>currentvalue:
            alist[poi] = alist[poi-gap]
            poi = poi-gap
        alist[poi] = currentvalue'''
#归并排序（归并是指将两个子列表合并成一个大的列表）
'''def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=k=j=0
        while i <len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i<len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j += 1
            k += 1
'''
#归并排序（pythonic）
'''def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    middle = len(alist)//2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right(0))
    merged.extend(right if right else left)
    return merged'''

#树
'''def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root'''
#链表实现树
'''class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    def getleftChild(self):
        return self.leftChild
    def setRootVal(self, obj):
        self.key = obj
    def getRootVal(self):
        return self.key

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getleftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

import operator
def evaluate(parseTree):
    opers = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.trudiv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.grtRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()'''
#树的遍历
'''def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal)
        inorder(tree.getRightChild)'''
#二叉堆
'''class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def perUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.perUp(self.currentSize)'''
#二叉搜索树
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
class TreeNode:
    def __init__(self, key, value, right=None, left=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.leftChild or self.rightChild)
    def hasAnyChildren(self):
        return self.rightChild and self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)
    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:#这里的for in 循环是一个递归调用
                    yield elem
            yield self.key#中序调用
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
