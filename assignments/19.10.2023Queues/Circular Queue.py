class MyCircularQueue:

    def __init__(self, k: int):
        self.cir_queue = list()
        self.count     = 0
        self.maxsize   = k

    def enQueue(self, value: int) -> bool:
        if self.count < self.maxsize:
            self.cir_queue.append(value)
            self.count += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.count != 0:
            self.cir_queue.pop(0)
            self.count -= 1
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.count != 0:
            return self.cir_queue[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.count != 0:
            return self.cir_queue[self.count-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxsize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()