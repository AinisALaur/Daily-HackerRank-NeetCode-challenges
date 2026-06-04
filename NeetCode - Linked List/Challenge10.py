class ListNode:
    def __init__(self, val, next, prev):
        self.val, self.next, self.prev = val, next, prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        newNode = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = newNode
        self.right.prev = newNode

        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        temp = self.left.next.next
        self.left.next = temp
        temp.prev = self.left

        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0
    

obj = MyCircularQueue(10)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)

print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
print(obj.Front())
