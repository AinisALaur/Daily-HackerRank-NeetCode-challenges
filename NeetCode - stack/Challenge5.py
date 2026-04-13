class MinStack:
    def __init__(self):
        self.minVals = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if(len(self.minVals) == 0):
            self.minVals.append(val)
            return

        minVal = min(self.minVals[-1], val)
        self.minVals.append(minVal)

    def pop(self) -> None:
        self.minVals.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minVals[-1]
    

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(0)
stack.push(-1)
stack.pop()
stack.pop()
stack.pop()
print(stack.getMin())