class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        n = len(target)
        z = max(target)

        while z:
            indexes = self.findAll(target, z)
            for i in indexes:
                if i - 1 in indexes:
                    continue
                for j in range(i, n):
                    if target[j] == z:
                        target[j] -= 1
                    else:
                        break
                res += 1
                # print(target)
            z -= 1
        
        return res

    def findAll(self, target, t):
        res = set()
        for idx, _ in enumerate(target):
            if _ == t:
                res.add(idx)
        return res