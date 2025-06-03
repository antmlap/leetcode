class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k            # Fixed-size list to hold queue elements
        self.size = k                  # Maximum capacity
        self.head = 0                  # Index of front element
        self.tail = 0                  # Next insert position
        self.count = 0                 # Number of elements in queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear_index = (self.tail - 1 + self.size) % self.size
        return self.q[rear_index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

