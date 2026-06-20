class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for i in range(k)]
        self.head = 0
        self.tail = -1
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.tail == -1:
            self.q[self.head] = value
            self.tail = self.head
            return True
        else:
            temp = self.tail + 1
            if temp == self.k:
                temp = 0
            if temp == self.head:
                return False
            self.q[temp] = value
            self.tail = temp
            return True

    def deQueue(self) -> bool:
        if self.tail == -1:
            return False
        
        if self.head == self.tail:
            self.q[self.head] = -1
            self.head = 0
            self.tail = -1
            return True
        
        temp = self.head + 1
        self.q[self.head] = -1
        self.head = 0 if temp == self.k else temp
        return True
            
        

    def Front(self) -> int:
        return self.q[self.head]

    def Rear(self) -> int:
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.tail == -1

    def isFull(self) -> bool:
        return (self.head == 0 and self.tail == self.k - 1) or (self.head == self.tail + 1)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()