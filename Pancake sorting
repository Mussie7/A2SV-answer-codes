class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []
        while not all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
            cur = max(arr)
            if arr.index(cur) + 1 == cur:
                arr = arr[:-1]
            elif arr.index(cur) + 1 != cur and len(arr) == 2:
                k.append(len(arr))
                arr.reverse()
            else:
                temp = arr[:arr.index(cur)+1]
                k.append(arr.index(cur)+1)
                temp.reverse()
                arr[:arr.index(cur)+1] = temp
                k.append(len(arr))
                arr.reverse()
                arr = arr[:-1]
        return k
