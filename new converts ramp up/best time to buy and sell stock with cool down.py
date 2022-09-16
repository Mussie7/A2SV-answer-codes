class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 2)
        prices.extend([0, 0])
        for i in reversed(range(n)):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                dp[i] = max(dp[i], prices[j] - prices[i] + dp[j+2])
                j += 1
            dp[i] = max(dp[i], dp[i+1])

        return dp[0]
