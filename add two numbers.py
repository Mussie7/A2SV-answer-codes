# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2 = "",""
        cur = l1
        while cur.next != None:
            num1 = str(cur.val) + num1
            cur = cur.next
        num1 = str(cur.val) + num1
        
        cur = l2
        while cur.next != None:
            num2 = str(cur.val) + num2
            cur = cur.next
        num2 = str(cur.val) + num2
        res = str(int(num1) + int(num2))
        res = res[::-1]
        
        l3 = ListNode()
        cur = l3
        for i in range(len(res)):
            cur.val = int(res[i])
            if i < len(res) - 1:
                cur.next = ListNode()
            cur = cur.next
        
        return l3
