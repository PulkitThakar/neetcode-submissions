class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                if dp[i - c] < float("inf"):
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        return -1 if dp[amount] == float("inf") else dp[amount]