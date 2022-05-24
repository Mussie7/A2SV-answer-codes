class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        tot = inf
        q = collections.deque()
        q.append(0)
            
        for i, num in enumerate(nums):
            prefix_sum.append(num + prefix_sum[-1])
            while q and prefix_sum[-1] <= prefix_sum[q[-1]]:
                q.pop()
            
            q.append(i+1)
            
            while q and prefix_sum[-1] - prefix_sum[q[0]] >= k:
                tot = min(tot, i+1 - q.popleft())
            
        
        return tot if tot != inf else -1
