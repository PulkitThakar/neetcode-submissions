class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visit = set()
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if(
                (i, j) in visit
                or i < 0 or i >= len(grid)
                or j < 0 or j >= len(grid[0])
                or grid[i][j] == "0"
            ):
                return
            
            visit.add((i, j))
            for di, dj in delta:
                dfs(i+di, j+dj)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands