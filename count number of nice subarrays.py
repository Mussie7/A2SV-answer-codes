class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = r = cnt = 0
        output = 0
        while r < len(nums):
            if cnt == k:
                record = l
                while not nums[l] % 2:
                    l += 1
                    output += 1
                output += 1
                l = record
            if not nums[r] % 2:
                r += 1
            elif nums[r] % 2 and cnt < k:
                r += 1
                cnt += 1
            elif nums[r] % 2 and cnt == k:
                while not nums[l] % 2:
                    l += 1
                l += 1
                cnt -= 1
        
        if cnt == k:
            while not nums[l] % 2:
                l += 1
                output += 1
            output += 1
        
        return output
