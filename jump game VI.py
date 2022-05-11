class Solution:    
    def maxResult(self, nums: List[int], k: int) -> int:
        q = collections.deque()
        q.append((nums[0],0))
        
        i = 1
        while i < len(nums):
            score = q[0][0] + nums[i]
            
            while q and q[-1][0] < score:
                q.pop()
            
            q.append((score,i))
            if q[0][-1] == i-k:
                q.popleft()
            
            i += 1
        
        return q[-1][0]
