class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            res = 0
            for i in range(l, r + 1):
                temp = nums[l - 1] * nums[i] * nums[r + 1]
                temp += dfs(l, i - 1)
                temp += dfs(i + 1, r)
                res = max(res, temp)
            
            dp[(l, r)] = res
            return dp[(l, r)]
        
        return dfs(1, len(nums) - 2)
            