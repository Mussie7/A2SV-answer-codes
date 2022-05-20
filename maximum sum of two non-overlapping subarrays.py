class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        l, r = 0, max(firstLen, secondLen)
        sum1= sum(nums[l:r])
        max_sum = 0
        while r <= len(nums):
            if len(nums) - r >= min(firstLen, secondLen):
                b = r
                f = b + min(firstLen, secondLen)
                sum2 = sum(nums[b:f])
                while f <= len(nums):
                    max_sum = max(sum1 + sum2, max_sum)
                    if f < len(nums):
                        sum2 += nums[f]
                    sum2 -= nums[b]
                    b += 1
                    f += 1
            if l >= min(firstLen, secondLen):
                b, f = 0, min(firstLen, secondLen)
                sum2 = sum(nums[b:f])
                while f <= l:
                    max_sum = max(sum1 + sum2, max_sum)
                    sum2 -= nums[b]
                    sum2 += nums[f]
                    b += 1
                    f += 1
            sum1 -= nums[l]
            if r < len(nums):
                sum1 += nums[r]
            l += 1
            r += 1
        
        return max_sum
