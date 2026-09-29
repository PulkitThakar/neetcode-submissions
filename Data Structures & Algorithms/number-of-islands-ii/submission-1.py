class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.par = [-1] * size
        self.count = 0
    
    def num_of_islands(self):
        return self.count
    
    def find(self, n):
        while self.par[n] != n:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return
        
        if self.rank[p1] >= self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        
        self.count -= 1

    def add_land(self, x):
        if self.par[x] >= 0:
            return
        
        self.par[x] = x
        self.rank[x] = 1
        self.count += 1
    
    def is_land(self, x):
        return self.par[x] >= 0


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dsu = UnionFind(m*n)
        answer = []
        
        for position in positions:
            land_position = position[0]*n + position[1]
            dsu.add_land(land_position)

            for d in delta:
                x = position[0] + d[0]
                y = position[1] + d[1]

                neighbor_position = x*n + y

                if (
                    x >= 0
                    and x < m
                    and y >=0
                    and y < n
                    and
                    dsu.is_land(neighbor_position)
                ):
                    dsu.union(land_position, neighbor_position)
                
            answer.append(dsu.num_of_islands())
                
        
        return answer