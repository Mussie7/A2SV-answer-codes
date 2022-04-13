class MinStack:

    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)

    def pop(self) -> None:
        self.__stack.pop()

    def top(self) -> int:
        
        return self.__stack[-1]

    def getMin(self) -> int:
        
        return min(self.__stack)
#         temp = self.__stack[-1]
#         for i in range(-2, -len(self.__stack) - 1, -1):
#             if self.__stack[i] < temp:
#                 temp = self.__stack[i]
        
#         return temp


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
