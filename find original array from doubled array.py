class Solution:
#     my original solution not fast enough
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         changed.sort()
#         original = []
#         checked = []
#         j = 0
#         for i in changed:
#             if i*2 in changed and i not in checked:
#                 original.append(i)
#                 checked.append(i*2)
#             elif i in checked:
#                 checked[j] = -1
#                 j += 1
#             else:
#                 return []
            
#         return original

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        l, r = 0, 1
        result = []
        while l < len(changed):
            if r <= l: r = l + 1

            if changed[l] == -1:
                l += 1
                continue

            while r < len(changed) and changed[r] != changed[l] * 2:
                r += 1
            if r == len(changed): return []

            changed[r] = -1
            result.append(changed[l])

            l += 1

        return result
