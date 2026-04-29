class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy less, sells high
        b = 0
        profit = 0
        for s in range(1, len(prices)):
            if prices[b] > prices[s]:
                b = s
            elif prices[b] < prices[s]:
                profit = max(profit, prices[s] - prices[b])
        return profit