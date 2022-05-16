# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        if head is None:
            return None
        
        l1 = ListNode()
        l1.val = cur.val
        
        while cur.next is not None:
            l2 = ListNode()
            l2.next = l1
            cur = cur.next
            l2.val = cur.val
            l1 = l2
        return l1
