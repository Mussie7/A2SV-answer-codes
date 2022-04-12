class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets.keys() and len(stack) == 0:
                return False
            else:
                if stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
