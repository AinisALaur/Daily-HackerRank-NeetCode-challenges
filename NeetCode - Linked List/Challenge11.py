class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key, self.val, self.next, self.prev = key, val, next, prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.left = ListNode()
        self.right = ListNode(0, 0, None, self.left)
        self.left.next = self.right
    
    def remove(self, curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def append(self, curr):
        prev = self.right.prev
        prev.next = curr
        self.right.prev = curr
        curr.prev = prev
        curr.next = self.right

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        
        temp = self.mapping[key]
        self.remove(temp)
        self.append(temp)

        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])

        if self.capacity == len(self.mapping) and key not in self.mapping:
            self.mapping.pop(self.left.next.key)
            self.remove(self.left.next)

        curr = ListNode(key, value, None, None)
        self.mapping[key] = curr
        self.append(curr)

    def print(self):
        curr = self.left.next
        while curr != self.right:
            print(curr.val)
            curr = curr.next


cache = LRUCache(2)
print(cache.get(2))
cache.put(2, 6)
print(cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(cache.get(1))
print(cache.get(2))
