class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[i])):
                self.matrix[i][j] += self.matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows = 0
        while row1 <= row2:
            if col1 == 0:
                rows += self.matrix[row1][col2]
            else:
                rows += (self.matrix[row1][col2] - self.matrix[row1][col1-1])
            row1 += 1

        return rows
