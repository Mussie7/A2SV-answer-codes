class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def bfs(i, j, dxn):
            visited, count = set(), 0
            q = deque()
            q.append((i, j))
            
            while q:
                level = len(q)
                count += 1
                
                for _ in range(level):
                    temp = q.popleft()
                    visited.add(temp)

                    for dx in dxn:
                        x, y = temp[0] + dx[0], temp[1] + dx[1]
                        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1 or (x, y) in visited:
                            continue

                        rotten[x][y] = count if not rotten[x][y] else min(rotten[x][y], count)
                        q.append((x, y))
        
        DXN = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rotten = [[0 if grid[i][j] == 1 else -1 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs(i, j, DXN)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if not rotten[i][j]:
                    return -1
                else:
                    ans = max(ans, rotten[i][j])
                    
        return ans
