class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        
        currSum = 0
        for i in nums:
            currSum += i
            if currSum > res:
                res = currSum
            if currSum < 0:
                currSum = 0
        
        return res