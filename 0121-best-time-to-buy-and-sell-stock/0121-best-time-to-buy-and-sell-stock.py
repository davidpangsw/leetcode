class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxAfter = [0] * n
        for i in range(n-2, -1, -1):
            maxAfter[i] = max(maxAfter[i+1], prices[i+1])
        
        maxProfit = 0
        for i, x in enumerate(prices):
            profit =  maxAfter[i] - prices[i] 
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

