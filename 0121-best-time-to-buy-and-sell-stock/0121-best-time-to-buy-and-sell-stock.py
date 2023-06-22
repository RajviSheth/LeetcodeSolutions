class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 999999
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = max(profit, prices[i] - minimum)
        return profit