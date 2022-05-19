class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        converted = 0
        ones = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and converted < k:
                r += 1
                converted += 1
            else:
                ones = max(r-l, ones)
                if nums[l] == 1:
                    l += 1
                else:
                    l += 1
                    converted -= 1
        
        ones = max(r-l, ones)
        return ones
