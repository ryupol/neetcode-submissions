class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 100 # maximum number possible

        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                res = max(res, sell - buy)

        return res