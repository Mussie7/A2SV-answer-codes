# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur, count, stack, twin_sum = head, 0, [], 0
        while cur:
            count += 1
            cur = cur.next
        
        cur = head
        i = 0
        while cur:
            if i >= count // 2:
                twin_sum = max(stack.pop() + cur.val, twin_sum)
            else:
                stack.append(cur.val)
            cur = cur.next
            i += 1
        
        return twin_sum
