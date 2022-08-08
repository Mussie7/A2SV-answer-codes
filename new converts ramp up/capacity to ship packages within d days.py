# Runtime: 412 ms, faster than 99.78% of Python3 online submissions for Capacity To Ship Packages Within D Days.
# Memory Usage: 17.1 MB, less than 81.80% of Python3 online submissions for Capacity To Ship Packages Within D Days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, capacity = max(weights), 0
        end = start * math.ceil(len(weights) / days)

        def check(cap):
            count, temp = 0, cap
            
            for weight in weights:
                temp -= weight
                if temp < 0:
                    count += 1
                    temp = cap - weight
                
                if count > days:
                    break
            count += 1
            
            return count <= days
        
        while start <= end:
            mid = start + (end-start) // 2
            
            if check(mid):
                capacity = mid
                end = mid - 1
            else:
                start = mid + 1
            
        return capacity
