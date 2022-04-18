class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        low, double = 0, 1
        result = []
        while low < len(changed):
            if double <= low:
                double = low + 1

            if changed[low] == -1:
                low += 1
                continue

            while double < len(changed) and changed[double] != changed[low] * 2:
                double += 1
            if double == len(changed):
                return []

            changed[double] = -1
            result.append(changed[low])

            low += 1

        return result
