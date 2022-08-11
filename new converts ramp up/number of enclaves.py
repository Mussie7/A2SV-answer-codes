class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, coordinates, dxn):
            nonlocal border, count
            
            i, j = coordinates
            if not i or not j or i == len(grid) - 1 or j == len(grid[0]) - 1:
                border = True
                
            grid[i][j] = 0
            count += 1
            for dx in dxn:
                x, y = i + dx[0], j + dx[1]
                
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                    continue
                dfs(grid, (x, y), dxn)
                            
        DXN = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                border = False
                count = 0
                if grid[i][j] == 1:
                    dfs(grid, (i, j), DXN)
                    if not border and count:
                        ans += count
        return ans
