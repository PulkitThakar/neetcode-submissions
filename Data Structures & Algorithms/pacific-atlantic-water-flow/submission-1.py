class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def dfs(i, j, prev, ocean):
            if (
                i < 0 or i >= m
                or j < 0 or j >= n
                or ocean[i][j] == 1
                or heights[i][j] < prev 
            ):
                return
            ocean[i][j] = 1
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(i + di, j + dj, heights[i][j], ocean)

        atl = [[0 for j in range(n)] for i in range(m)]
        pac = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, n-1, heights[i][n-1], atl)
        
        for j in range(n):
            dfs(0, j, heights[0][j], pac)
            dfs(m-1, j, heights[m-1][j], atl)

        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] == 1 and atl[i][j] == 1:
                    res.append([i, j])
        return res