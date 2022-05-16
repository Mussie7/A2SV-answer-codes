# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        while cur is not None:
            count += 1
            cur = cur.next
        
        cur = head
        res = ListNode(cur.val)
        for j in range(k-1):
            cur = cur.next
            res = ListNode(cur.val, res)
        
        i = 0
        cur2 = res
        while i < count // k - 1:
            while cur2.next is not None:
                cur2 = cur2.next
            
            cur = cur.next
            cur2.next = ListNode(cur.val) 
            for j in range(k-1):
                cur = cur.next
                cur2.next = ListNode(cur.val,cur2.next)
            
            i += 1
        
        while cur2.next is not None:
            cur2 = cur2.next
        
        cur = cur.next
        while cur is not None:
            cur2.next = ListNode(cur.val)
            cur2 = cur2.next
            cur = cur.next
        
        return res
