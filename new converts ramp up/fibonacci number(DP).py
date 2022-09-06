class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        memoize = [-1] * (n + 1)
        memoize[0], memoize[1] = 0, 1
        def recur(i):
            if memoize[i] >= 0:
                return memoize[i]
            
            memoize[i] = recur(i - 1) + recur(i - 2)
            return memoize[i]
        
        recur(n)
        return memoize[n]
