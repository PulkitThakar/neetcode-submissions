class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for i in range(n + 1)]
        dp[0] = 0

        i = 1
        while i*i <= n:
            coin = i * i
            for j in range(coin, n + 1):
                dp[j] = min(dp[j], dp[j-coin] + 1)
            i += 1
        return dp[n]