from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original = []
        checked = {}
        c = Counter(changed)
        c = dict(c)
        if len(changed) % 2 != 0:
            return original
        for i in changed:
            if i == 0 and c[0] % 2 != 0:
                return []
            if i*2 in c and i not in checked:
                original.append(i)
                if i*2 in checked:
                    checked[i*2] += 2
                else:
                    checked[i*2] = 1
            elif i*2 in c and checked[i] == -1:
                original.append(i)
                if i*2 in checked:
                    checked[i*2] += 2
                else:
                    checked[i*2] = 1
            elif i in checked and checked[i] > 0:
                checked[i] += -2
            else:
                return []
        
        if max(checked.values()) > 0:
            return []
        return original
