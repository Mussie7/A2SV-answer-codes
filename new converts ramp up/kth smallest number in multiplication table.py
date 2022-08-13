class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num):
            count, low, high = 0, min(m, n), max(m, n)
            for i in range(1, low + 1):
                count += min(num // i, high)
            
            return count >= k
        
        start, end = 1, k
        while start < end:
            mid = start + (end - start) // 2
            
            if enough(mid):
                end = mid
            else:
                start = mid + 1
        
        return start
