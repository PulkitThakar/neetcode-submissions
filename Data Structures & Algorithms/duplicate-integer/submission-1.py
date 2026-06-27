class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        z = set(nums)
        return not len(z) == len(nums)