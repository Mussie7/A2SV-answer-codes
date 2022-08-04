class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        temp = [heapq.heappop(arr) for j in range(n)]
        arr.extend(temp)
        temp = []

    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        heapq.heapify(arr)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        self.heapify(arr, n, 0)
