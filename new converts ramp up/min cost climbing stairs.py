class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(i: int) -> int:
            if i >= len(cost):
                return 0
            
            if memoize[i] > 0:
                return memoize[i]
            
            memoize[i] = cost[i] + min(minCost(i + 1), minCost(i + 2))
            return memoize[i]
        
        
        memoize = [-1] * len(cost)
        
        return min(minCost(0), minCost(1))
