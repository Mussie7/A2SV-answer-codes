# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur = head
        stack, answer = [], []
        while cur:
            answer.append(0)
            cur = cur.next
        
        cur = head
        i = 0
        while cur:
            while stack and stack[-1][1].val < cur.val:
                temp = stack.pop()
                answer[temp[0]] = cur.val
            stack.append((i,cur))
            cur = cur.next
            i += 1
        
        return answer
