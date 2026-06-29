class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while j > 0 and not s[j].isalnum():
                j -= 1
            while i < len(s) and not s[i].isalnum():
                i += 1
            
            if j >= 0 and i < len(s) and s[i] != s[j]:
                return False
            
            j -= 1
            i += 1
        return True