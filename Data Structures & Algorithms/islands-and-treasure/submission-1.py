class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        steps = 0
        
        while q:
            steps += 1
            z = len(q)
            while z:
                i, j = q.popleft()
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    newI, newJ = i + di, j + dj
                    if newI in range(m) and newJ in range(n) and grid[newI][newJ] == 2147483647:
                        grid[newI][newJ] = steps
                        q.append([newI, newJ])
                z -= 1

