class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        ans = 0
        for i in range(m):
            start = 0
            end = n - 1
            best = n
            
            while start <= end:
                mid = start + (end-start)//2
                if grid[i][mid] < 0:
                    best = mid
                    end = mid - 1
                else:
                    start = mid + 1
            
            ans += (n - best) * (m - i)
            n = best
            if not n:
                break
                
        return ans
