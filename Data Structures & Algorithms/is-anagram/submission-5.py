class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        alphabet_count = [0]*26
        ord_a = ord('a')
        for i in range(len(s)):
            alphabet_count[ord(s[i]) - ord_a] += 1
            alphabet_count[ord(t[i]) - ord_a] -= 1
        
        return not any(alphabet_count)