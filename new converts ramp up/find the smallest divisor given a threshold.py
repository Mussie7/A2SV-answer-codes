class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
    
        def check(thre: int) -> bool:
            return sum([math.ceil(num/thre) for num in nums]) <= threshold
        
        while start <= end:
            mid = start + (end-start) // 2
            
            if check(mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return ans
