class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = []
        operator = False
        second = ""
        
        # organize the input and make the divisions and multiplications first
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if stack and not operator and s[i].isnumeric():
                if stack[-1].isnumeric():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
            elif stack and s[i] == "*" or s[i] == "/":
                operation.append(s[i])
                operator = True
            elif stack and operator:
                if i < len(s)-1 and s[i+1].isnumeric():
                    second += s[i]
                else:
                    second += s[i]
                    temp = int(stack.pop())
                    if operation[-1] == "*":
                        res = temp * int(second)
                        stack.append(str(res))
                    else:
                        res = temp // int(second)
                        stack.append(str(res))
                    second = ""
                    operator = False
            else:
                stack.append(s[i])
        
        # now that it is organized do the addition and subtraction
        another = []
        for i in stack:
            if i == "+" or i == "-":
                operation.append(i)
                operator = True
            elif another and operator:
                temp = int(another.pop())
                if operation[-1] == "+":
                    res = temp + int(i)
                    another.append(str(res))
                else:
                    res = temp - int(i)
                    another.append(str(res))
                operator = False
            else:
                another.append(i)
        
        return another[-1]
