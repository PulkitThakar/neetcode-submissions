class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x != 0:
            t = math.fmod(x, 10)
            x = int(x/10)

            if res > int(MAX/10) or (res == int(MAX/10) and t > math.fmod(MAX, 10)):
                return 0
            
            if res < int(MIN/10) or (res == int(MIN/10) and t < math.fmod(MIN, 10)):
                return 0
            
            res = int(res * 10 + t)
        
        return res