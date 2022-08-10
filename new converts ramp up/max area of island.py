class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area, visited = 0, set([])
        DIRECTION = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(grid, direction, coordinates):
            i, j = coordinates
            m, n = len(grid), len(grid[0])
            
            nonlocal visited
            
            if (i, j) in visited:
                return
            visited.add(coordinates)

            for dx in direction:
                x = i + dx[0]
                y = j + dx[1]
                
                if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                    continue
                    
                dfs(grid, direction, (x, y))
        
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    prev = len(visited)
                    dfs(grid, DIRECTION, (i, j))
                    area = max(area, len(visited) - prev)

        return area
