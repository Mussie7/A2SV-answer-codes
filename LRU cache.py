class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.stack = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.stack.remove(key)
            self.stack.append(key)
            return self.dic[key]
        
        return-1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)
        elif self.capacity:
            self.dic[key] = value
            self.capacity -= 1
            self.stack.append(key)
        else:
            self.dic.pop(self.stack.pop(0))
            self.dic[key] = value
            self.stack.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
