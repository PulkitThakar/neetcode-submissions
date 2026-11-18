class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        
        sec_last, last = 0, nums[0]

        for i in range(1, len(nums)):
            temp = max(last, sec_last + nums[i])
            sec_last = last
            last = temp
        
        return last