class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        output, sub = 0, 1
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                sub += 1
            else:
                output += sub * (sub + 1) // 2
                sub = 1
                
        output += sub * (sub + 1) // 2
        return output
