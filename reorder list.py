# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mod = slow.next
        slow.next = None
        l1 = None
        while mod:
            l1 = ListNode(mod.val, l1)
            mod = mod.next
        
        cur = head
        while l1:
            cur.next = ListNode(l1.val, cur.next)
            cur = cur.next.next
            l1 = l1.next
            
        """
        Do not return anything, modify head in-place instead.
        """
