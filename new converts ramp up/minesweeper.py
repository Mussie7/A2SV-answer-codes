class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def dfs(board, click, dxn):
            i, j = tuple(click)
            if board[i][j].isnumeric() or board[i][j] == "B" or board[i][j] == "X":
                return
            
            if board[i][j] == "M":
                board[i][j] = "X"
            
            elif board[i][j] == "E":
                count = 0
                m, n = len(board), len(board[0])
                for dx in dxn:
                    x, y = i + dx[0], j + dx[1]
                    
                    if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != "M":
                        continue
                    else:
                        count += 1
                if count:
                    board[i][j] = str(count)
                else:
                    board[i][j] = "B"
                    for dx in dxn:
                        x, y = i + dx[0], j + dx[1]
                        
                        if x < 0 or y < 0 or x >= m or y >= n:
                            continue
                        dfs(board, [x, y], dxn)
        
        
        DXN = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dfs(board, click, DXN)
        
        return board
