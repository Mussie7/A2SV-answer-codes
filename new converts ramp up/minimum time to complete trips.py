class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start = min(time)
        end = min(start * totalTrips, max(time) * math.ceil(totalTrips / len(time)))
        ans = 0
        while start <= end:
            mid = start + (end-start) // 2
            total = totalTrips
            for i in range(len(time)):
                total -= mid // time[i]
                if total <= 0:
                    break
            
            if total > 0:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        
        return ans
