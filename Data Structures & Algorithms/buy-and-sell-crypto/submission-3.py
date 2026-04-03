class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) is 0:
            return 0

        least_value = float('inf')
        max_profit = 0

        for price in prices:
            if price < least_value:
                least_value = price
            else:
                profit = price - least_value

                if profit > max_profit:
                    max_profit = profit
        
        return max_profit