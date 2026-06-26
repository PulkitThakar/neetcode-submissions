class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.points:
            self.points[tuple(point)] += 1
        else:
            self.points[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        res = 0
        for p in self.points:
            i, j = p[0], p[1]
            x, y = point[0], point[1]
            if i != x and j != y and (i, y) in self.points and (x, j) in self.points:
                res += (self.points[(i,j)]*self.points[(i,y)]*self.points[(x,j)])
        return res