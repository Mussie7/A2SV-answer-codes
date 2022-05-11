class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not len(nums) % 2:
            return True
        return self.getMaxScore(nums,0,len(nums)-1) >= 0
    
    def getMaxScore(self, nums, s, e):
        if s == e:
            return nums[s]
        
        first = nums[s] - self.getMaxScore(nums,s+1,e)
        last = nums[e] - self.getMaxScore(nums,s,e-1)

        return max(first,last)
