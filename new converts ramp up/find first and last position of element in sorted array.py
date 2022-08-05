class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        ans.append(self.binarySearch(nums, target, True))
        if ans[0] == -1:
            ans.append(-1)
        else:
            ans.append(self.binarySearch(nums, target))
        
        return ans
    
    def binarySearch(self, nums: List[int], target: int, first: bool = False) -> int:
        start = 0
        end = len(nums)-1
        res = -1
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                res = mid
                if first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return res
