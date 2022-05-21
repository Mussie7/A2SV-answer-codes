class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if len(security) <= time * 2:
            return []
        
        dec = []
        inc = []
        for i in range(time+1):
            while dec and security[i] > dec[-1]:
                dec.pop()
            dec.append(security[i])
            while inc and security[i+time] < inc[-1]:
                inc.pop()
            inc.append(security[i+time])
        
        r = time
        output = []
        while r < len(security) - time:
            if security[r] == dec[-1] == inc[0] and len(dec) == len(inc) == time+1:
                output.append(r)
            
            if dec[0] == security[r-time]:
                dec.pop(0)
            if inc[0] == security[r]:
                inc.pop(0)
                
            if r < len(security) - time - 1:
                while dec and security[r+1] > dec[-1]:
                    dec.pop()
                dec.append(security[r+1])

                while inc and security[r+time+1] < inc[-1]:
                    inc.pop()
                inc.append(security[r+time+1])
            r += 1
        
        return output
