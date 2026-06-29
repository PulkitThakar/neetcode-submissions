class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        q = [[grid[0][0], 0, 0]]

        while q:
            wei, i, j = heapq.heappop(q)
            if (i, j) in visit:
                continue
            if i == m - 1 and j == n - 1:
                return wei
            visit.add((i, j))
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newI, newJ = i + di, j + dj
                if (newI in range(m)) and (newJ in range(n)) and ((newI, newJ) not in visit):
                    heapq.heappush(q, [max(wei, grid[newI][newJ]), newI, newJ])
        
        return -1
                