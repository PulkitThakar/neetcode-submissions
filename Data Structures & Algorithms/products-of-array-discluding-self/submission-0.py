class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * res[-1])
        
        temp = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] = res[i] * temp
            temp *= nums[i]
        
        return res