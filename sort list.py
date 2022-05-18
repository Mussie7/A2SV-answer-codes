# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sortHead(head)
     
    
    def sortHead(self, head):
        if not head or not head.next:
            return head
        
        slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        first = self.sortHead(head)
        second = self.sortHead(temp)
        
        return self.merge(first, second)
    
    def merge(self, l1, l2):
        l3 = ListNode()
        cur1 = l1
        cur2 = l2
        
        if not cur1 and not cur2:
            return None
        
        cur = l3
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.val = cur1.val
                cur1 = cur1.next
            else:
                cur.val = cur2.val
                cur2 = cur2.next
            cur.next = ListNode()
            cur = cur.next
        
        if cur1:
            x = cur1
        elif cur2:
            x = cur2
        
        while x.next:
            cur.val = x.val
            x = x.next
            cur.next = ListNode()
            cur = cur.next
        cur.val = x.val
        
        return l3
