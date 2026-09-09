class StockSpanner:

    def __init__(self):
        self.prev = []
        self.span = []
        self.n = 0
    
    def next(self, price: int) -> int:
        self.prev.append(price)
        self.n += 1
        if not self.span or self.prev[self.n - 2] > price:
            self.span.append(1)
        else:
            z = self.n - 2
            res = 1
            while z >= 0 and self.prev[z] <= price:
                res += self.span[z]
                z -= self.span[z]
            self.span.append(res)
        return self.span[-1]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)