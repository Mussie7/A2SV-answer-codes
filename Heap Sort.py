class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        index = 0
        while 2*index + 1 < n - i:
            if 2*index + 2 < n-i:
                if arr[index] < arr[2*index+1]:
                    if arr[2*index+1] >= arr[2*index+2]:
                        arr[index], arr[2*index+1] = arr[2*index+1], arr[index]
                        index = 2*index + 1
                    else:
                        arr[index], arr[2*index+2] = arr[2*index+2], arr[index]
                        index = 2*index + 2
                elif arr[index] < arr[2*index+2]:
                    arr[index], arr[2*index+2] = arr[2*index+2], arr[index]
                    index = 2*index + 2
                else:
                    break
            else:
                if arr[index] < arr[2*index+1]:
                    arr[index], arr[2*index+1] = arr[2*index+1], arr[index]
                    index = 2*index + 1
                else:
                    break
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n-1, 0, -1):
            if arr[i] > arr[(i-1)//2]:
                arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
                j = i
                while 2*j+2 < n or 2*j+1 < n:
                    if 2*j+2 < n:
                        if arr[j] < arr[2*j+1]:
                            if arr[2*j+1] >= arr[2*j+2]:
                                arr[j], arr[2*j+1] = arr[2*j+1], arr[j]
                                j = 2*j+1
                            else:
                                arr[j], arr[2*j+2] = arr[2*j+2], arr[j]
                                j = 2*j+2
                        elif arr[j] < arr[2*j+2]:
                            arr[j], arr[2*j+2] = arr[2*j+2], arr[j]
                            j = 2*j+2
                        else:
                            break
                    else:
                        if arr[j] < arr[2*j+1]:
                            arr[j], arr[2*j+1] = arr[2*j+1], arr[j]
                            j = 2*j+1
                        else:
                            break

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(1, n):
            arr[0], arr[-i] = arr[-i], arr[0]
            self.heapify(arr, n, i)
