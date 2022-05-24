class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        k_sum = []
        window, win_sum = 1, 0 
        for i in range(len(nums)):
            win_sum += nums[i]
            if window >= k:
                k_sum.append(win_sum)
                win_sum -= nums[i+1-k]
            window += 1
        
        left = [0] * len(k_sum)
        right = [0] * len(k_sum)
        l, r = 0, len(k_sum) - 1
        for i in range(len(k_sum)):
            if k_sum[i] > k_sum[l]:
                l = i
            left[i] = l
            if k_sum[len(k_sum)-(i+1)] >= k_sum[r]:
                r = len(k_sum)-(i+1)
            right[len(k_sum)-(i+1)] = r
            
        ans = []
        for m in range(k, len(k_sum) - k):
            l, r = left[m-k], right[m+k]
            if not ans or (k_sum[l]+k_sum[m]+k_sum[r] > k_sum[ans[0]] + k_sum[ans[1]] + k_sum[ans[2]]):
                ans = [l, m, r]
        
        return ans
