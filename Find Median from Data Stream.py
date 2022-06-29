class MedianFinder:
    def __init__(self):
        self.heap = []
        
    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        self.heap.sort()
        median = (self.heap[ceil(len(self.heap)/2) - 1] + self.heap[floor(len(self.heap)/2)]) / 2
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# faster code with heap(2 heaps)
# class MedianFinder:
    
#     def __init__(self):
#         self.small = []
#         self.large = []
        
#     def addNum(self, num: int) -> None:
#         if len(self.small) == len(self.large):
#             heappush(self.large, -heappushpop(self.small, -num))
#         else:
#             heappush(self.small, -heappushpop(self.large, num))

#     def findMedian(self) -> float:
#         if len(self.small) == len(self.large):
#             return (self.large[0] - self.small[0]) / 2
#         else:
#             return float(self.large[0])
