class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)     
        
        return -heapq.nsmallest(k, nums)[-1]
