class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        div = 1
        while x // (div * 10):
            div *= 10
        
        while x:
            l = x // div
            r = x % 10
            if l != r:
                return False
            
            x = x % div
            x = x // 10
            div = div // 100
        
        return True