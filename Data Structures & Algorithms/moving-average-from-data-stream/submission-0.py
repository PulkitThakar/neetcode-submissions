class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.q = deque()
        self.res = 0

    def next(self, val: int) -> float:
        if self.count == self.size:
            self.res = self.res - self.q[0]
            self.q.popleft()
        else:
            self.count += 1
        
        self.q.append(val)
        self.res = self.res + val
        return self.res / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
