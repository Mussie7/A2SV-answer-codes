# Runtime: 27 ms, faster than 99.56% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.9 MB, less than 39.64% of Python3 online submissions for Remove Duplicate Letters.

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = dict(Counter(s))
        stack, visited = [], set()
        for i in range(len(s)):
            c[s[i]] -= 1
            
            if s[i] in visited:
                continue
                
            while stack and s[i] < stack[-1]:
                if c[stack[-1]] > 0:
                    visited.remove(stack.pop())
                else:
                    break
            
            stack.append(s[i])
            visited.add(s[i])
        
        return ''.join(stack)
