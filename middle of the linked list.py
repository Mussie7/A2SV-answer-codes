# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        counter = 0
        cur = head
        while cur.next is not None:
            counter += 1
            cur = cur.next
        counter += 1
        
        cur = head
        for i in range(counter // 2):
            cur = cur.next
        
        return cur
    
    # A better code with two pointers
#     class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         slow = fast = head
#         fast = fast.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         if fast:
#             return slow.next
#         return slow
