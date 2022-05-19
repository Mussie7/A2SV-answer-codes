# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            k = self.mergeTwoLists(lists.pop(), lists.pop())
            while lists:
                k = self.mergeTwoLists(k, lists.pop())
            return k
        
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return list1 or list2
        
        head = cur = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
        
            cur = cur.next
        
        cur.next = list1 or list2
        
        return head.next
