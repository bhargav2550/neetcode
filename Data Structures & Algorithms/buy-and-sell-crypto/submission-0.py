class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxs = 0
        for i in range(len(prices)):
            l = min(l,prices[i])
            maxs = max(maxs, prices[i] - l)
        return 0 if maxs < 0 else maxs
