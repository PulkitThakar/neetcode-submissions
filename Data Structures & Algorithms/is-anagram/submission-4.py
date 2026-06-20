class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        if len(s) != len(t):
            return False
        
        mismatch = 0;
        for i in range(len(s)):
            if d[s[i]] == 0:
                mismatch += 1
            d[s[i]] += 1;
            if d[s[i]] == 0:
                mismatch -= 1
            
            if d[s[i]] == 0:
                mismatch += 1
            d[t[i]] -= 1;
            if d[t[i]] == 0:
                mismatch -=1
        
        return mismatch == 0