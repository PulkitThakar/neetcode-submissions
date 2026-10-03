class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        
        l, r = 0, n-1
        t, b = 0, n-1

        i = 1
        while l <= r and t <= b:
            j = l
            while j <= r:
                res[t][j] = i
                j += 1
                i += 1
            t += 1

            j = t
            while j <= b:
                res[j][r] = i
                j += 1
                i += 1
            r -= 1
            
            if l > r or t > b or i > n**2:
                break
            
            j = r
            while j >= l:
                res[b][j] = i
                j -= 1
                i += 1
            b -= 1
            
            j = b
            while j >= t:
                res[j][l] = i
                j -= 1
                i += 1
            l += 1

        return res