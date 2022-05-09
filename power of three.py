class Solution:
    def __init__(self):
        self.x = 0
        
        
    def isPowerOfThree(self, n: int) -> bool:
        k = n
        return self.cubeChecker(k, n)
        
    
    def cubeChecker(self, k, n):
        
        if k < 3:
            return 3**self.x == float(n)
        elif k%3 != 0.0:
            return False
        else:
            self.x += 1
            return self.cubeChecker(k/3, n)
