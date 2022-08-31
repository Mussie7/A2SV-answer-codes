class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dic = {"R": set(), "D": set()}
        r, d = deque([]), deque([])
        
        for i in range(len(senate)):
            dic[senate[i]].add(i)
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        
        if not d:
            return "Radiant"
        
        if not r:
            return "Dire"
        
        while d and r:
            for i in range(len(senate)):
                if senate[i] == "R":
                    if i in dic["R"] and d:
                        dic["D"].remove(d[0])
                        d.popleft()
                    if not d:
                        return "Radiant"
                else:
                    if i in dic["D"] and r:
                        dic["R"].remove(r[0])
                        r.popleft()
                    if not r:
                        return "Dire"
                
                if r[0] == i:
                    r.append(r.popleft())
                
                if d[0] == i:
                    d.append(d.popleft())
