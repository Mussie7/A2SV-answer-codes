# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        l3 = ListNode()
        cur1 = list1
        cur2 = list2
        
        if cur1 is None and cur2 is None:
            return None
        
        cur = l3
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                cur.val = cur1.val
                cur1 = cur1.next
            else:
                cur.val = cur2.val
                cur2 = cur2.next
            cur.next = ListNode()
            cur = cur.next
        
        if cur1 is not None:
            x = cur1
        elif cur2 is not None:
            x = cur2
        
        while x.next is not None:
            cur.val = x.val
            x = x.next
            cur.next = ListNode()
            cur = cur.next
        cur.val = x.val
        
        return l3
