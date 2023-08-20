class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 999999
        profit = 0
        for index in range(len(prices)):
            if prices[index] < minimum:
                minimum = prices[index]
            else:
                profit = max(profit, prices[index] - minimum)
                
        return profit