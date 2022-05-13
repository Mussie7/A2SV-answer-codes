class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x = self.wierdShit(n)
        return x[k-1]
    
    
    def wierdShit(self,n):
        if n == 1:
            return "0"
        else:
            x = self.wierdShit(n-1)
            return x + "1" + self.reverse(self.invert(x))
            
    
    def reverse(self, st: str) -> str:
            return st[::-1]
        
    
    def invert(self, st: str) -> str:
            st_list = list(st)
            for i in range(len(st_list)):
                if st_list[i] == "0":
                    st_list[i] = "1"
                else:
                    st_list[i] = "0"
            
            return "".join(st_list)
