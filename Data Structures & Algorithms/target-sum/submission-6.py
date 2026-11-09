class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            if index == len(nums):
                return 1 if target == curr_sum else 0

            result = (
                backtrack(index + 1, curr_sum + nums[index])
                + backtrack(index + 1, curr_sum - nums[index])
            )
            memo[(index, curr_sum)] = result
            return result
        
        return backtrack(0, 0)