# Runtime: 94 ms, faster than 98.85% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 14.7 MB, less than 96.82% of Python3 online submissions for Minimum Path Sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1:
                    dp[j] = grid[i][j] + dp[j + 1]
                    dp[-1] = inf
                    continue
                dp[j] = grid[i][j] + min(dp[j], dp[j+1])
            
        return dp[0]
