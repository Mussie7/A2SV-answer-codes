class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.Power(x,n,n)
    
    def Power(self, x, n, check = 1):
        if n == 0:
            return 1
        if check == -1:
            return 1/x
        elif abs(n) == 1:
            return x
        elif n > 0:
            if not n % 2:
                y = x**2
                return self.Power(y, n//2)
            else:
                return x * self.Power(x, n-1)
        else:
            if x >= check and check != 2*32:
                x = 1/x
                check = 2*32
            if not n % 2:
                y = x**2
                return self.Power(y, n//2, check)
            else:
                return x * self.Power(x, n+1, check)
