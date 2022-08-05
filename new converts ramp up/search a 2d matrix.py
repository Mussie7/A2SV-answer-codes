class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m-1
        while start < end:
            mid = start + math.ceil((end - start) / 2)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid

        idx = start
        start, end = 0, n-1
        while start <= end:
            mid = start + (end-start) // 2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False
