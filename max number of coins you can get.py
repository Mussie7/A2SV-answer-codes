class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coin = 0
        for i in range(len(piles)//3):
            pile_tuple = (piles.pop(-1), piles.pop(-1), piles.pop(0))
            max_coin += pile_tuple[1]
        
        return max_coin
