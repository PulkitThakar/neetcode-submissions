class Solution:
    def hammingWeight(self, n: int) -> int:
        n = (0xFFFFFFFF & n)
        res = 0
        while n > 0:
            res += (n & 1)
            n = (n >> 1) & 0xFFFFFFFF
        
        return res;
