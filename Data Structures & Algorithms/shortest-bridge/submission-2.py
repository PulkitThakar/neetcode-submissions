class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1 = set()
        island2 = set()
        visit = set()

        def dfs(i, j, island):
            if (
                i < 0 or i >= len(grid)
                or j < 0 or j >= len(grid[0])
                or grid[i][j] == 0
                or (i, j) in visit
            ):
                return
            
            island.add((i, j))
            visit.add((i, j))
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(i + di, j + dj, island)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit and grid[i][j] == 1:
                    dfs(i, j, island1)
                    break
            if island1:
                break

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit and grid[i][j] == 1:
                    dfs(i, j, island2)
                    break
            if island2:
                break
        
        if len(island2) < len(island1):
            island1, island2 = island2, island1
        
        q = deque()
        visit = set(island1)
        for i in island1:
            q.append(i)
        
        steps = 0
        while (q):
            n = len(q)
            while n > 0:
                n = n - 1
                i, j = q.popleft()
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if (i + di, j + dj) in island2:
                        return steps
                    if (
                        0 <= i + di < len(grid)
                        and 0 <= j + dj < len(grid[0])
                        and (i + di, j + dj) not in visit
                        and grid[i + di][j + dj] == 0
                    ):
                        visit.add((i + di, j + dj))
                        q.append((i + di, j + dj))
            steps += 1
        return -1