class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        ans = 0
        while start <= end:
            mid = start + (end-start) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        
        return ans
        
        # negative marking - violates the constraints but it is faster and real interesting
        # for i in range(len(nums)):
        #     if nums[abs(nums[i])] < 0:
        #         ans = abs(nums[i])
        #         break
        #     nums[abs(nums[i])] = -nums[abs(nums[i])]
        
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])
        
        # return ans
