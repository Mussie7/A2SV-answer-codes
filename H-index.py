class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        lt, rt = -1, 0
        
        while rt < len(citations):
            if citations[rt] <= len(citations) - rt:
                lt = citations[rt]
            elif citations[rt] >= len(citations) - rt and len(citations) - rt > lt:
                lt = len(citations) - rt
            else:
                break
            rt += 1
            
        return lt
