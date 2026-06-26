class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1

            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newI, newJ = i + di, j + dj
                if (
                    newI in range(len(matrix))
                    and newJ in range(len(matrix[0]))
                    and matrix[newI][newJ] < matrix[i][j]
                ):
                    res = max(res, 1 + dfs(newI, newJ))
            
            dp[(i, j)] = res
            return res
        
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        
        return res