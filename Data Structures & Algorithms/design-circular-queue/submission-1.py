class MyCircularQueue:

    def __init__(self, k: int):
        self.stackA = []
        self.stackB = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.stackA) + len(self.stackB) == self.k:
            return False
        self.stackA.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return False
        if len(self.stackB) == 0:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        self.stackB.pop()
        return True

    def Front(self) -> int:
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return -1
        if len(self.stackB) == 0:
            return self.stackA[0]
        return self.stackB[-1]

    def Rear(self) -> int:
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return -1
        if len(self.stackA) == 0:
            return self.stackB[0]
        return self.stackA[-1]

    def isEmpty(self) -> bool:
        return len(self.stackA) == 0 and len(self.stackB) == 0

    def isFull(self) -> bool:
        return len(self.stackA) + len(self.stackB) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()