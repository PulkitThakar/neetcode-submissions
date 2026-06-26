class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0 for i in range(26)]
            for c in s:
                tmp = ord(c) - ord('a')
                count[tmp] += 1
            key = ""
            for c in count:
                key += chr(c)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values())