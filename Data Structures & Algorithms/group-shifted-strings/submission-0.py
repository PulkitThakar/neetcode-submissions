class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                d[(0)].append(s)
                continue
            
            key = []
            for i in range(0, len(s) - 1):
                l = ord(s[i])
                r = ord(s[i + 1])
                if l < r:
                    key.append(r - l)
                else:
                    key.append(26 + r - l)
            d[tuple(key)].append(s)

        return list(d.values())