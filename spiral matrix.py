class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        column, row = 0, 0
        m, n = len(matrix), len(matrix[0])
        k, j = 0, 0
        while len(output) < m*n:
            column = k
            while column < n-k and len(output) < m*n:
                output.append(matrix[row][column])
                column += 1            
            k += 1
            j += 1
            row = j

            while row < m-j+1 and len(output) < m*n:
                output.append(matrix[row][column-1])
                row += 1
            
            row -= 1
            column -= 1
            while column > k-1 and len(output) < m*n:
                output.append(matrix[row][column-1])
                column -= 1
            
            row -= 1
            while row >= j and len(output) < m*n:
                output.append(matrix[row][column])
                row -= 1
            
            row = j
                        
        return output 
