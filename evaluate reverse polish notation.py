class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            elif i.startswith('-') and len(i) > 1:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    if a * b < 0:
                        res = ceil(a / b)
                    else:
                        res = floor(a / b)
                    stack.append(res)

        return stack[0]
