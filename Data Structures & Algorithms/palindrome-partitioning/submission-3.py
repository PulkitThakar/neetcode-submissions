class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def backtracking(i):
            if i == len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    backtracking(j+1)
                    part.pop()
            
        backtracking(0)
        return res
    
    def isPalin(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True