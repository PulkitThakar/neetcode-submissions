class Solution:
    def isPalindrome(self, x: int) -> bool:
        left_div = 1
        while left_div * 10 <= x:
            left_div *= 10
        
        while x:
            left = x // left_div
            right = x % 10
            if left != right:
                return False
            x = x % left_div
            x = x // 10
            left_div = left_div / 100
            
        return True