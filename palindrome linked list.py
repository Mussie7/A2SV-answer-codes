# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        stack = []        
        cur = head
        i = 0
        while cur:
            if i >= count // 2:
                if count % 2 and i == count // 2:
                    cur = cur.next
                    i += 1
                    continue
                if stack and stack[-1] == cur.val:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur.val)
            cur = cur.next
            i += 1
        
        return True
