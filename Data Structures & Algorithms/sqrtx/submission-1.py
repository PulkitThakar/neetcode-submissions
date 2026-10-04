class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i = 1
        while (i + 1)**2 <= x:
            i += 1
        
        return i