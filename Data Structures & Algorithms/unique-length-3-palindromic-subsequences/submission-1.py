class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = {}
        right = {}

        for i in s:
            left[i] = left.get(i, 0)
            right[i] = 1 + right.get(i, 0)
        
        left[s[0]] += 1
        right[s[0]] -= 1
        res = set()
        for i in range(1, len(s) - 1):
            right[s[i]] -= 1
            for c in left:
                if right[c] > 0 and left[c] > 0:
                    res.add(f"{c}{s[i]}{c}")
            left[s[i]] += 1
        return len(res)