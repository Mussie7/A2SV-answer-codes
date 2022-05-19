class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit = {}
        variety = total = l = r = 0
        while r < len(fruits):
            if fruits[r] in fruit and variety <= 2:
                fruit[fruits[r]] += 1
                r += 1
            elif fruits[r] not in fruit and variety < 2:
                fruit[fruits[r]] = 1
                variety += 1
                r += 1
            else:
                total = max(total, sum(fruit.values()))
                while 0 not in fruit.values():
                    fruit[fruits[l]] -= 1
                    l += 1
                temp = list(fruit.keys())
                i = 0
                while i < len(temp):
                    if fruit[temp[i]] == 0:
                        del fruit[temp[i]]
                        variety -= 1
                    i += 1
        
        total = max(total, sum(fruit.values()))
        return total
