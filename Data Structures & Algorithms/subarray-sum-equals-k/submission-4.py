class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = { 0:1 }
        res = 0
        curr = 0
        for i in nums:
            curr += i
            res += d.get(curr - k, 0)
            d[curr] = 1 + d.get(curr, 0)
        return res
