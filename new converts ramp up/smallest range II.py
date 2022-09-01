class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        smallest = nums[0] + k
        largest = nums[-1] - k

        for i in range(len(nums)-1):
            ans = min(ans, max(largest, nums[i]+k) - min(smallest, nums[i+1] - k))
        
        return ans
