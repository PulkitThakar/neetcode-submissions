class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            key = tuple(key)
            res[key] = res.get(key, [])
            res[key].append(s)
        
        return list(res.values())