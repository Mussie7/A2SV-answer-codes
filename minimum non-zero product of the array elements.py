class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        x = 2**p
        y = 1000000007
        return pow(x-2,x//2-1,y) * (x-1) % y
