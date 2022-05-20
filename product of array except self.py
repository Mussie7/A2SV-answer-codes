class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = nums[:]
        suf = nums[:]
        for i in range(1, len(nums)):
            pre[i] *= pre[i-1]
            suf[-i - 1] *= suf[-i]
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(suf[i+1])
            elif i == len(nums)-1:
                output.append(pre[i-1])
            else:
                output.append(pre[i-1]*suf[i+1])
        return output
