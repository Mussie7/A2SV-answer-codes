class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        i = 0
        while i < len(nums):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            if i < len(nums)-1:
                right_sum -= nums[i+1]
            i += 1

        return -1
