class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_value = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if least_value > prices[i]:
                least_value = prices[i]
            
            profit = max(profit, prices[i] - least_value)
        
        return profit