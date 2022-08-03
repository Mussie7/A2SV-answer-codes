class MedianFinder:

    def __init__(self):
        self.firsthalf = []
        self.secondhalf = []

    def addNum(self, num: int) -> None:
        if len(self.firsthalf) == len(self.secondhalf):
            temp = heapq.heappushpop(self.secondhalf, num)
            heapq.heappush(self.firsthalf, -temp)
        else:
            temp = heapq.heappushpop(self.firsthalf, -num)
            heapq.heappush(self.secondhalf, -temp)

    def findMedian(self) -> float:
        if len(self.firsthalf) > len(self.secondhalf):
            return float(-self.firsthalf[0])
        return (-self.firsthalf[0] + self.secondhalf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
