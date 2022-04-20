class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = []
        for i in range(len(position)):
            distance = target - position[i]
            time = distance / speed[i]
            pos_time.append((position[i], time))
        pos_time.sort(reverse=True)
        stack = []
        stack.append(pos_time.pop())
        while pos_time:
            temp = pos_time.pop()
            if temp[1] < stack[-1][1]:
                stack.append(temp)
            else:
                while stack and temp[1] >= stack[-1][1]:
                    stack.pop()
                stack.append(temp)
        return len(stack)
