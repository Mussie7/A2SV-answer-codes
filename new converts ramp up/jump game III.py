class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = {start}
        
        if not arr[start]:
            return True
        
        while q:
            ind = q.popleft()
            if not arr[ind]:
                return True
            
            if ind - arr[ind] >= 0 and ind - arr[ind] not in visited:
                visited.add(ind - arr[ind])
                q.append(ind - arr[ind])
            
            if ind + arr[ind] < len(arr) and ind + arr[ind] not in visited:
                visited.add(ind + arr[ind])
                q.append(ind + arr[ind])
        
        return False
