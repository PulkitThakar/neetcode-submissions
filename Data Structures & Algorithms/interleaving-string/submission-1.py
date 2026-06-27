class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = {(len(s1), len(s2)): True}

        def helper(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = False
            if i == len(s1):
                if s3[i + j] == s2[j]:
                    res = helper(i, j+1)
                else:
                    res = False
            
            elif j == len(s2):
                if s3[i + j] == s1[i]:
                    res = helper(i + 1, j)
                else:
                    res = False
            
            elif s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                res = helper(i + 1, j) or helper(i, j + 1)
            
            elif s1[i] == s3[i + j]:
                res = helper(i + 1, j)

            elif s2[j] == s3[i + j]:
                res = helper(i, j + 1)
            
            else:
                res = False
            
            dp[(i, j)] = res
            return res
            
        return helper(0, 0)