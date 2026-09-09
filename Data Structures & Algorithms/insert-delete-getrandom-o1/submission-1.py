class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        self.num_map[val] = self.n
        self.n += 1
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        
        ind = self.num_map[val]
        self.num_list[ind] = self.num_list[self.n-1]
        self.num_map[self.num_list[self.n-1]] = ind
        self.num_map.pop(val, None)
        self.num_list.pop()
        self.n -= 1
        return True
        

    def getRandom(self) -> int:
        res = random.randrange(self.n)
        return self.num_list[res]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()