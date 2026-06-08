class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val, self.prev, self.next = val, prev, next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRigth(Val)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfuCount = 0
        self.valMap = {}
        self.countMap = collections.defaultdict(int)
        self.listMap = collections.defaultdict(LinkedList)

    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[count].pop(key)
        self.listMap[count + 1].pushRight(key)
        
        if count == self.lfuCount and self.listMap[count].length() == 0:
            self.lfuCount += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key not in self.valMap and len(self.valMap) == self.capacity:
            res = self.listMap[self.lfuCount].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)


        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])





# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)