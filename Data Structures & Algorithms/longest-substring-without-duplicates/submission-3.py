class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        res = 0
        i = 0
        for j in range(len(s)):
            while s[j] in s_set:
                s_set.remove(s[i])
                i += 1
            s_set.add(s[j])
            res = max(res, j - i + 1)
        
        return res