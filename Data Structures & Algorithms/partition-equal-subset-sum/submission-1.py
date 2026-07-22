class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        n = int((s / 2))
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in nums:
            for j in range(n, i - 1, -1):
                if dp[j - i]:
                    dp[j] = True
            if dp[n]:
                return True
        
        return False