class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.buildHeap(stones)
        while len(stones) > 1:
            stone1, stone2 = self.heappop(stones), self.heappop(stones)
            if stone1 > stone2:
                self.heappush(stones, stone1-stone2)

        return stones[0] if stones else 0
    
    #build a max heap
    def buildHeap(self, heap):
        n = len(heap)
        for i in range(n - 1, 0, -1):
            if heap[i] > heap[(i - 1) // 2]:
                heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
                j = i
                branch1, branch2 = 2 * j + 1, 2 * j + 2
                while branch1 < n:
                    if branch2 < n and heap[j] < heap[branch1]:
                        if heap[branch1] >= heap[branch2]:
                            heap[j], heap[branch1] = heap[branch1], heap[j]
                            j = branch1
                        else:
                            heap[j], heap[branch2] = heap[branch2], heap[j]
                            j = branch2
                    elif branch2 < n and heap[j] < heap[branch2]:
                        heap[j], heap[branch2] = heap[branch2], heap[j]
                        j = branch2
                    elif branch2 >= n and heap[j] < heap[branch1]:
                        heap[j], heap[branch1] = heap[branch1], heap[j]
                        j = branch1
                    else:
                        break
                    branch1, branch2 = 2 * j + 1, 2 * j + 2

    # build a push function for the max heap
    def heappush(self, heap, value):
        heap.append(value)
        i = len(heap) - 1
        while i:
            if heap[i] > heap[(i-1)//2]:
                heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
                i = (i-1)//2
            else:
                break
                
    # build a pop fuction for the max heap
    def heappop(self, heap):
        heap[0], heap[-1] = heap[-1], heap[0]
        output = heap.pop()
        j, n = 0, len(heap)
        branch1, branch2 = 2 * j + 1, 2 * j + 2
        while branch1 < n:
            if branch2 < n and heap[j] < heap[branch1]:
                if heap[branch1] >= heap[branch2]:
                    heap[j], heap[branch1] = heap[branch1], heap[j]
                    j = branch1
                else:
                    heap[j], heap[branch2] = heap[branch2], heap[j]
                    j = branch2
            elif branch2 < n and heap[j] < heap[branch2]:
                heap[j], heap[branch2] = heap[branch2], heap[j]
                j = branch2
            elif branch2 >= n and heap[j] < heap[branch1]:
                heap[j], heap[branch1] = heap[branch1], heap[j]
                j = branch1
            else:
                break
            branch1, branch2 = 2 * j + 1, 2 * j + 2

        return output
