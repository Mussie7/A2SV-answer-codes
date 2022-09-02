class Solution:
    def paintJob(self, n, arr):
        arr.sort()
        red, blue = arr[-1], arr[0] + arr[1]
        
        l, r = 2, n - 2
        while r > n // 2:
            if red > blue:
                print("Yes")
                return
            
            red += arr[r]
            blue += arr[l]
            l += 1
            r -= 1
        
        if red > blue:
            print("Yes")
        else:
            print("No")
    
        
 
j = Solution()
rep = int(input())
for _ in range(rep):
    n = int(input())
    arr = list(map(int, input().split()))
    j.paintJob(n, arr)
