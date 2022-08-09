class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = {}
        visited = set([])
        
        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            stack = [i]
            while stack:
                temp = stack.pop()
                for j in range(len(isConnected)):
                    if isConnected[temp][j] == 1:
                        if j in visited:
                            continue
                        
                        if i not in province:
                            province[i] = {j}
                        else:
                            province[i].add(j)
                        
                        visited.add(j)
                        if j != temp:
                            stack.append(j)
            
            visited.add(i)
        
        return len(province)
