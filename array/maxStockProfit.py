class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profit_array=[0]*(len(prices)-1)
        for i in range(len(prices)-1):
            profit_array[i]= prices[i+1]-prices[i]
        for i in range(len(profit_array)):
            profit = max(profit, (profit+profit_array[i]))
        return profit
            
        
