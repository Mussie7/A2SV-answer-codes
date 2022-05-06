class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        num_list = list(num)
        while num_list:
            while stack and k and int(stack[-1]) > int(num_list[0]):
                stack.pop()
                k -= 1
            if stack or int(num_list[0]):
                stack.append(num_list.pop(0))
            else:
                num_list.pop(0)
        
        if k:
            stack = stack[:-k]
        
        return "".join(stack) or "0"
