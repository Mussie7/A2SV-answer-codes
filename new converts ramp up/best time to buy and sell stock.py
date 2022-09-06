class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMax = [0] * (len(prices) + 1)
        cur, ans = inf, 0
        
        for i in range(len(prices)-1, -1, -1):
            curMax[i] = max(prices[i], curMax[i + 1])
        
        for i in range(len(prices)):
            if prices[i] > cur:
                continue
            cur = min(cur, prices[i])
            ans = max(ans, curMax[i] - cur)

        return ans
      
# better code
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         cur, ans = inf, 0
#         for price in prices:
#             cur = min(cur, price)
#             ans = max(price - cur, ans)

#         return ans
