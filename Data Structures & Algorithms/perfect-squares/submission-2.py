class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for i in range(n + 1)]
        dp[0] = 0
        j = 1
        while j*j <= n:
            c = j*j
            for i in range(c, n + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)
            j += 1
            # print(dp)
        
        return dp[n] if dp[n] != float("inf") else -1