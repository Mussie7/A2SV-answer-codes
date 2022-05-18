# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                head = cur.next
                cur = head
            else:
                break
        
        while cur and cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur
                cur = cur.next
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                temp.next = cur.next
                cur = temp
            else:
                cur = cur.next
        
        return head
