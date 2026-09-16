class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, n in enumerate(nums):
            if target - n in d:
                return [d[target-n], idx]
            d[n] = idx
        return [-1, -1]