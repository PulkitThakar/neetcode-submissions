class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i - 1 in s:
                continue
            else:
                temp = 1
                j = i + 1
                while j in s:
                    j += 1
                    temp += 1
                res = max(res, temp)
        return res