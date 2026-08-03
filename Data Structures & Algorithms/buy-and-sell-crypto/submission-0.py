class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 100
        
        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                profit = max(profit, sell - buy)

        return profit