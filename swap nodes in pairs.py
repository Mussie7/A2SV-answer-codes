# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = head.next
        head.next = head.next.next
        temp.next = head
        head = temp
        
        cur = head.next
        while cur.next and cur.next.next:
            temp1 = cur.next
            temp2 = temp1.next
            temp1.next = temp2.next
            temp2.next = temp1
            cur.next = temp2
            cur = temp1
        
        return head
