class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = { 0:1 }
        res = 0
        curr = 0
        for i in nums:
            curr += i
            if curr - k in d:
                res += d[curr - k]
            if curr not in d:
                d[curr] = 0
            d[curr] += 1
        return res
