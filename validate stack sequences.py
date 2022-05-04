class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lt, rt = 0, 0
        while lt < len(pushed):
            
            while pushed and pushed[lt] == popped[rt]:
                pushed.pop(lt)
                if lt:
                    lt -= 1
                rt += 1
            
            lt += 1
        
        return rt == len(popped)
