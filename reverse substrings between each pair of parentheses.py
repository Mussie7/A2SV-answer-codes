class Solution:
    def reverseParentheses(self, s: str) -> str:
        opening = s.split("(")
        stack = []
        for i in opening:
            if ")" not in i:
                stack.append(i)
            else:
                while ")" in i:
                    reverse = i[:i.find(")")]
                    reverse = reverse[::-1]
                    i = reverse + i[i.find(")")+1:]
                    i = stack.pop() + i
                stack.append(i)
        
        return stack[0]
