from collections import Counter
 
class Solution:
    def power_up(self, n, arr):
        c = Counter(arr)
        d = len(c)
        
        if d == n:
            return ((str(d) + " ") * (d-1)) + str(d)
            
        output = (str(d) + " ") * d
        
        ex = [str(d + (i + 1)) + " " for i in range(n - d - 1)]
        output += "".join(ex)
        output += str(n)
        return output
        
 
j = Solution()
rep = int(input())
for _ in range(rep):
    n = int(input())
    arr = input().split()
    print(j.power_up(n, arr))
