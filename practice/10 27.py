#bubble
def bubble(li):
    count = len(li)-1
    while count > 0:
        for i in range(count):
            if li[i+1] < li[i]:
                tmp = li[i]
                li[i] = li[i+1]
                li[i+1] = tmp
        count -= 1
#selection
def select(li):
    for i in range(len(li)):
        min = li[i]
        index = i
        for k in range(i+1, len(li)):
            if li[k] < min:
                min = li[k]
                index = k
        li[index] = li[i]
        li[i] = min
#insert
def insert(li):
    for i in range(len(li)):
        now = li[i]
        for k in range(i):
            if li[k] > li[i]:
                li.pop(i)
                li.insert(k, now)
                break
#quick
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while low < high:
        while low < high and array[high] > key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= key:
            low += 1
        array[high] = array[low]
    array[high] = key
    quick_sort(array, left, low - 1)
    quick_sort(array, low + 1, right)


#merger
def merger(li):
    if len(li) <= 1:
        return li
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]
    nleft = merger(left)
    nright = merger(right)
    return merges(nleft, nright)

def merges(a, b):
    tmp = []
    h=j=0
    while h < len(a) and j < len(b):
        if a[h] < b[j]:
            tmp.append(a[h])
            h += 1
        else:
            tmp.append(b[j])
            j += 1
    if h == len(a):
        for i in b[j:]:
            tmp.append(i)
    else:
        for i in a[h:]:
            tmp.append(i)
    return tmp
#radix
def radix(li):
    layers = len(str(max(li)))
    i = 0
    while i < layers:
        bucket = [[] for _ in range(10)]
        for x in li:
            bucket[int(x//10**i)%10].append(x)
        li.clear()
        for k in bucket:
            for h in k:
                if h != '':
                    li.append(h)
        i += 1
#test
import random
a = [random.randint(0,101) for _ in range(random.randrange(5, 11))]
print(f'原始数组：{a}')
print(f'排序后数组：{sorted(a)}')
quick_sort(a, 0 ,len(a)-1)
print(f'算法得数组：{a}')