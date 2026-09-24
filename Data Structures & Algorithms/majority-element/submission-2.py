class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n = len(nums)
        return nums[(n // 2)]