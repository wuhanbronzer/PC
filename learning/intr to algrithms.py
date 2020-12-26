#insertion-sort
#升序
'''class sort_algri:
    def __init__(self,lis):
        self.lis = list(lis)

    def ascending(self):
        target = self.lis
        for i in range(len(target)-1, -1, -1):
            key = target[i]
            j = i + 1
            while j < len(target) and target[j] < key:
                target[j-1] = target[j]
                j += 1
            target[j-1] = key
        return target


a = sort_algri([11111,11,1111,234,66,9,44,10])
print(a.ascending())
'''
#Poker牌堆合并问题
#MERGE


'''def merge(li1, li2):
    source_lis1 = list(li1)
    source_lis2 = list(li2)
    source_lis1.append(9999)
    source_lis2.append(9999)
    target = []
    i = 0
    j = 0
    for k in range(len(source_lis1)+len(source_lis2)-1):
        if i < len(source_lis1) and source_lis1[i] <= source_lis2[j]:
            target.append(source_lis1[i])
            i = i + 1 if i+1 < len(source_lis1) else i
        elif j < len(source_lis2) and source_lis2[j] < source_lis1[i]:
            target.append(source_lis2[j])
            j += 1
    target.pop(-1)
    return target


a = [1, 2, 3, 4, 5,19]
b = [7,11, 14, 22, 27]
print(merge(a,b))'''
