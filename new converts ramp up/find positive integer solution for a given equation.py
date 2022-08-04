"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x_val = 1
        
        while x_val < 1000:
            if customfunction.f(x_val, 1) > z:
                break
                
            start, end = 1, 1000
            while start <= end:
                mid = start + (end-start)// 2
                if customfunction.f(x_val, mid) == z:
                    ans.append([x_val, mid])
                    break
                elif customfunction.f(x_val, mid) < z:
                    start = mid + 1
                else:
                    end = mid - 1
            
            x_val += 1
        
        return ans
