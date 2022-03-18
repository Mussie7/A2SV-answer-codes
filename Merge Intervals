class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) == 1:
            return intervals
        else:
            intervals.sort()
            temp = intervals[0]
            intervals.pop(0)
            while len(intervals) > 0:
                if temp[1] >= intervals[0][0]:
                    temp[1] = max(temp[1], intervals[0][1])
                    intervals.pop(0)
                else:
                    result.append(temp)
                    temp = intervals[0]
                    intervals.pop(0)
                if len(intervals) == 0:
                    result.append(temp)
        return result
