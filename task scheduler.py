from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        max_freq = max(c.values())
        res = (max_freq - 1) * (n + 1)
        frequent_freq = Counter(c.values())[max_freq]
        res += frequent_freq
        res = max(res, len(tasks))
        return res
