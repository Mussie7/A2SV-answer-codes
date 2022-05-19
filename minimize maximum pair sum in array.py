class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        paired_nums = []
        for i in range(len(nums) // 2):
            paired_nums.append(nums[i] + nums[len(nums)-(i+1)])
        ans = max(paired_nums)
        return ans
