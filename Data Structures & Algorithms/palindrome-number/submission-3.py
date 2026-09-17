class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        d = 1
        while x // (d * 10) != 0:
            d *= 10
        
        while x:
            l = x // d
            r = x % 10
            if l != r:
                return False
            x = x % d
            x = x // 10
            d = d // 100
        
        return True