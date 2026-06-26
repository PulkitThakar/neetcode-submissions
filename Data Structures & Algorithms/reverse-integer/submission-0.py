class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        
        res = 0
        while x:
            res *= 10
            res += x%10
            x = x//10
            if res not in range(-pow(2, 31), pow(2, 31)):
                return 0
        
        return -res if negative else res
