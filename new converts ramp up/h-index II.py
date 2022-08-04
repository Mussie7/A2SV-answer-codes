class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start, end = 0, len(citations) - 1
        best = 0
        while start <= end:
            mid = start + (end-start) // 2
            if citations[mid] >= len(citations) - mid:
                best = max(best, len(citations) - mid)
                end = mid - 1
            else:
                best = max(best, citations[mid])
                start = mid + 1
        
        return best
