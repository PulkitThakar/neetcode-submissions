class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        if n == 2:
            return 0 if prices[0] > prices[1] else prices[1] - prices[0]
        
        buy = [0 for i in range(n)]
        sell = [0 for i in range(n)]

        for i in range(n):
            if i == 0:
                buy[i] = -prices[i]
            elif i == 1:
                buy[i] = max(buy[i-1], -prices[i])
                sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            else:
                buy[i] = max(buy[i-1], sell[i-2] - prices[i])
                sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        
        return sell[n - 1]