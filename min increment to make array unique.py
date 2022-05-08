class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res, low = 0, -2
        
        for i in nums:
            low = max(low+1, i)
            res += low - i
        
        return res
