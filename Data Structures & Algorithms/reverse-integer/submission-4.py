class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        
        x = abs(x)
        # [-2,147,483,648, 2,147,483,647]

        res = 0
        while x:
            if res > 214748364:
                return 0
            
            i = x % 10
            x //= 10
            if res == 214748364:
                if (neg and i > 8) or i > 7:
                    return 0
            res = (res * 10) + i


        return -res if neg else res