class Node:
    def __init__(self, key, val, pre = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def add(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.nxt = node
        node.nxt = nxt
        node.prev = prev
        nxt.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            del self.cache[lru.key]
            self.remove(lru)