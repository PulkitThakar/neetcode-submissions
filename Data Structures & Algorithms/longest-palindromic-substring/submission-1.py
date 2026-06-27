class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resJ = 0
        resK = 0
        for i in range(n):
            j, k = i, i
            while(
                j >= 0 and j < n
                and k >= 0 and k < n
                and s[j] == s[k]
            ):
                if resK - resJ < k - j:
                    resK = k
                    resJ = j
                j -= 1
                k += 1
        
        for i in range(n):
            j, k = i, i + 1
            while(
                j >= 0 and j < n
                and k >= 0 and k < n
                and s[j] == s[k]
            ):
                if resK - resJ < k - j:
                    resK = k
                    resJ = j
                j -= 1
                k += 1

        return s[resJ:resK+1]