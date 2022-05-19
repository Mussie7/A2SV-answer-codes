class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        c = Counter(nums)
        x = c.most_common()
        for i in range(len(x)):
            if x[i][1] > 1:
                temp = x[i][1] - 1
                count += int(temp * (temp + 1) / 2)
                
        return count
