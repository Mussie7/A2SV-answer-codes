class Solution:
    def RAMDownload(self, n, k, arr):
        arr.sort()
        for i in range(n):
            if arr[i][0] <= k:
                k += arr[i][1]
            else:
                break
        
        return k
    
        
 
j = Solution()
rep = int(input())
for _ in range(rep):
    first = tuple(input().split())
    n, k = int(first[0]), int(first[1])
    second = input().split()
    third = input().split()
    arr = []
    for i in range(n):
        arr.append([int(second[i]), int(third[i])])
    
    print(j.RAMDownload(n, k, arr))
