class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, coordinates, dxn):
            i, j = coordinates
            board[i][j] = "B"
            
            for dx in dxn:
                x, y = i + dx[0], j + dx[1]
                if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != "O":
                    continue
                dfs(board, (x, y), dxn)
        
        
        DXN = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(board, (i, 0), DXN)
                
            if board[i][len(board[0]) - 1] == "O":
                dfs(board, (i, len(board[0]) - 1), DXN)

        for j in range(1, len(board[0]) - 1):
            if board[0][j] == "O":
                dfs(board, (0, j), DXN)
            
            if board[len(board) - 1][j] == "O":
                dfs(board, (len(board) - 1, j), DXN)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                
                if board[i][j] == "B":
                    board[i][j] = "O"
