# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            cur = lst
            while cur:
                heap.append(cur.val)
                cur = cur.next
                
        heapq.heapify(heap)
        head = cur = ListNode()
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        
        return head.next
