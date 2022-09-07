class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.extend([0, 0])
        maxNum = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            nums[i] += maxNum
            maxNum = max(maxNum, nums[i + 1])
        
        return max(nums[0], nums[1])
