class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.top, self.persons = [], {}
        self.times = times
        
        for i in range(len(times)):
            if persons[i] in self.persons:
                self.persons[persons[i]] += 1
            else:
                self.persons[persons[i]] = 1
            
            if not self.top:
                self.top.append(persons[i])
            elif self.persons[persons[i]] >= self.persons[self.top[-1]]:
                self.top.append(persons[i])
            else:
                self.top.append(self.top[-1])
            
    def q(self, t: int) -> int:
        start, end = 0, len(self.top) - 1
        while start < end:
            mid = start + math.ceil((end-start) / 2)
            if self.times[mid] == t:
                return self.top[mid]
            elif self.times[mid] > t:
                end = mid - 1
            else:
                start = mid
        
        return self.top[start]
                


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
