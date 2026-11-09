class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = [{} for i in range(len(nums) + 1)]
        def backtrack(index, curr_sum):
            if curr_sum in memo[index]:
                return memo[index][curr_sum]
            if index == len(nums):
                return 1 if target == curr_sum else 0

            result = (
                backtrack(index + 1, curr_sum + nums[index])
                + backtrack(index + 1, curr_sum - nums[index])
            )
            memo[index][curr_sum] = result
            return result
        
        return backtrack(0, 0)