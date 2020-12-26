#第二题：辆数相加
'''class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = []
        a2 = []
        conti = True
        while conti:
            if l1.next == None:
                if l1.val:
                    a1.append(l1.val)
                conti = False
            else:
                a1.append(l1.val)
                l1 = l1.next
        fir_num = 0
        for i in range(len(a1)):
            fir_num += a1[i]*(10**i)
        conti = True
        while conti:
            if l2.next == None:
                if l2.val:
                    a2.append(l2.val)
                conti = False
            else:
                a2.append(l2.val)
                l2 = l2.next
        sec_num = 0
        for i in range(len(a2)):
            sec_num += a2[i]*(10**i)
        new_li = str(fir_num + sec_num)
        ans = ListNode(int(new_li[0]))
        head = ListNode(None)
        head.next = ans
        print(f'a1是{a1}，a2是{a2}')
        print(f'第一个数是{fir_num}，第二个数是{sec_num}，和是{new_li}')
        if len(new_li) > 1:
            for i in range(1,len(new_li)):
                a = head.next
                b = ListNode(int(new_li[i]))
                head.next = b
                b.next = a
            return b
        else:
            return ans


l12 = ListNode(0)
l12.next = ListNode(7)
l21 = ListNode(0)
l21.next = ListNode(8)

S = Solution()
a = S.addTwoNumbers(l1=l12, l2=l21)
print('---------')
print(a.val)
a = a.next
print(a.val)
a = a.next
'''
#第一题：两数之和
#大神代码
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        size = 0
        while size < len(nums):
            if target-nums[size] in d:
                if d[target-nums[size]] < size:
                    return [d[target-nums[size]],size]
            else:
                d[nums[size]] = size
            size = size + 1


