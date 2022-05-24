class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 1
        sub = 1
        q1 = collections.deque()
        q2 = collections.deque()
        q1.append(0)
        q2.append(0)
        while r < len(nums):
            if nums[q2[0]] - nums[q1[0]] <= limit:
                sub = max(sub, r - l)
            else:
                l += 1
                if l > q1[0]:
                    q1.popleft()
                if l > q2[0]:
                    q2.popleft()
            
            while q1 and nums[r] < nums[q1[-1]]:
                q1.pop()
            while q2 and nums[r] > nums[q2[-1]]:
                q2.pop()
            
            q1.append(r)
            q2.append(r)
            
            r += 1
            
        return max(sub, r-l) if nums[q2[0]] - nums[q1[0]] <= limit else sub
