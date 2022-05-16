# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 0
        cur = head
        while cur.next is not None:
            counter += 1
            cur = cur.next
        counter += 1
        
        cur = head
        for i in range(counter - n - 1):
            cur = cur.next
        
        if counter == n:
            head = head.next
        else:
            cur.next = cur.next.next
        
        return head
