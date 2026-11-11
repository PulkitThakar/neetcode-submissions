class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while q and fresh:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in delta:
                    x, y = i + di, j + dj
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == 1:
                            grid[x][y] = 0
                            fresh -= 1
                            q.append((x, y))
                            if fresh == 0:
                                return time
        
        return time if fresh == 0 else -1
