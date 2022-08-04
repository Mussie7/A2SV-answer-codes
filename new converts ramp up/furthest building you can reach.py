class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap = []
        i = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                ladders -= 1
                heapq.heappush(minheap, diff)
            
                if ladders < 0:
                    bricks -= heapq.heappop(minheap)
            
            if bricks < 0:
                break
        
        return i-1 if bricks < 0 else i
