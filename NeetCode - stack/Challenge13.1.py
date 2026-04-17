class FreqStack:
    def __init__(self):
        self.mostFrequent = [-1, -1, -1]
        self.freq = {}
        self.index = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = [1, [self.index]]
        else:
            self.freq[val][0] += 1
            self.freq[val][1].append(self.index)


        if self.freq[val][0] > self.mostFrequent[1] or (self.freq[val][0] == self.mostFrequent[1] and self.freq[val][1][-1] > self.mostFrequent[2]):
            self.mostFrequent = [val, self.freq[val][0], self.index]

        self.index += 1

    def pop(self) -> int:
        toReturn = self.mostFrequent[0]
        self.freq[self.mostFrequent[0]][0] -= 1;

        self.freq[self.mostFrequent[0]][1].pop();
        self.mostFrequent[1] -= 1
        self.mostFrequent[2] = (
            self.freq[self.mostFrequent[0]][1][-1]
            if len(self.freq[self.mostFrequent[0]][1]) > 0
            else -1
        )

        for key, val in self.freq.items():
            if(key != self.mostFrequent[0]):
                if val[0] > self.mostFrequent[1] or (len(val[1]) > 0 and val[0] == self.mostFrequent[1] and val[1][-1] > self.mostFrequent[2]):
                    self.mostFrequent = [key, val[0], val[1][-1]]

        return toReturn
    
stack = FreqStack()
stack.push(5) #0
stack.push(7) #1
stack.push(5) #2
stack.push(7) #3
stack.push(4) #4
stack.push(5) #5

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())