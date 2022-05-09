class Solution:
    def __init__(self):
        self.x = 0
        
        
    def isPowerOfFour(self, n: int) -> bool:
        k = n
        return self.forthChecker(k, n)
        
    
    def forthChecker(self, k, n):
        if k < 4:
            return 4**self.x == float(n)
        elif k%4 != 0.0:
            return False
        else:
            self.x += 1
            return self.forthChecker(k/4, n)
