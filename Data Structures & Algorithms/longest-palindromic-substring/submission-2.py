class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_j = -1
        res_k = -1
        for i in range(len(s)):
            j = i
            k = i
            while j >=0 and k < len(s) and s[j] == s[k]:
                if res < k - j + 1:
                    res = k - j + 1
                    res_j = j
                    res_k = k
                j -= 1
                k += 1
        
        for i in range(len(s)):
            j = i
            k = i + 1
            while j >=0 and k < len(s) and s[j] == s[k]:
                if res < k - j + 1:
                    res = k - j + 1
                    res_j = j
                    res_k = k
                j -= 1
                k += 1
        
        return s[res_j:res_k+1]