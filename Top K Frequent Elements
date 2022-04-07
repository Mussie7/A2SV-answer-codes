from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        freq = c.most_common()
        for i in range(k):
            res.append(freq[i][0])
        
        return res
