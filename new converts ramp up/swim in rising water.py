class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h, visited = [], {(0, 0)}
        t = grid[0][0]
        heapq.heappush(h, (t, 0, 0))
        DXN = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        while h:
            temp = heapq.heappop(h)
            t = max(t, temp[0])
            
            if (temp[1], temp[2]) == (len(grid) - 1, len(grid) - 1):
                return t
            
            for dxn in DXN:
                i, j = temp[1] + dxn[0], temp[2] + dxn[1]
                
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid) or (i, j) in visited:
                    continue
                
                visited.add((i, j))
                heapq.heappush(h, (grid[i][j], i, j))
