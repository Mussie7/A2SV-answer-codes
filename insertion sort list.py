# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        l1 = ListNode(head.val)
        cur = head.next
        while cur:
            if cur.val <= l1.val:
                temp = ListNode(cur.val,l1)
                l1 = temp
            else:
                cur1 = l1
                while cur1.next and cur1.next.val < cur.val:
                    cur1 = cur1.next
                cur1.next = ListNode(cur.val,cur1.next)
            cur = cur.next
        
        return l1
