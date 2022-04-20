class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_index = []
        stack = []
        answer = [0] * len(temperatures)
        for i in range(-1 , -len(temperatures)-1, -1):
            temp_index.append((temperatures[i], i + len(temperatures)))
        stack.append(temp_index.pop())
        while temp_index:
            if temp_index[-1][0] < stack[-1][0]:
                stack.append(temp_index.pop())
            else:
                while stack and temp_index[-1][0] > stack[-1][0]:
                    answer[stack[-1][1]] = temp_index[-1][1] - stack[-1][1]
                    stack.pop()
                stack.append(temp_index.pop())
        
        return answer
