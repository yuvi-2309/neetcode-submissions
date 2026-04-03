class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = {}
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    if arr.get(prices[i]) is not None:
                        if arr[prices[i]] < prices[j]:
                            arr[prices[i]] = prices[j]
                    else:
                        arr[prices[i]] = prices[j]
                
        lookup = []
        for key, value in arr.items():
            difference = value - key
            if (difference > 0):
                lookup.append(difference)
        
        greatest_value = 0
        for i in lookup:
            if i > greatest_value:
                greatest_value = i
        
        return greatest_value