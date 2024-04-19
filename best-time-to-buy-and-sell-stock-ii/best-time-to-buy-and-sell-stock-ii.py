class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 1
        profit = 0
        while curr < len(prices):
            if prices[curr-1] > prices[curr]:
                curr += 1
            else:
                profit += prices[curr] - prices[curr-1]
                curr += 1
                
        return profit
                
                
                
                
            
                
        