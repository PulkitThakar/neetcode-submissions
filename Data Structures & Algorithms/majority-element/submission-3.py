class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = (len(nums) // 2) + 1
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
            if d[i] == n:
                return i
        return -1
            