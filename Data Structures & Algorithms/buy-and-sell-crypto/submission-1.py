class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_value:
                min_value = price
            else:
                profit = price - min_value

                if profit > max_profit:
                    max_profit = profit
        
        return max_profit