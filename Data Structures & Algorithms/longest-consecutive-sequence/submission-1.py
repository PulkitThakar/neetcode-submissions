class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in s:
            if i - 1 not in s:
                j = i
                while j in s:
                    j += 1
                res = max(res, j - i)
        
        return res