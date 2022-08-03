class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        row = k // n + 1 if k % n else k // n
        col = k % n if k % n else n
        
        for i in range(row):
            heap += [-num for num in matrix[i]]
                
        heapq.heapify(heap)
        
        for i in range(n-col):
            heapq.heappop(heap)

        j = row
        while j < len(matrix) and -heap[0] > matrix[j][0]:
            for i in range(n):
                if -heap[0] < matrix[j][i]:
                    break
                heapq.heappush(heap, -matrix[j][i])
                heapq.heappop(heap)
            j += 1
        
        return -heap[0]
