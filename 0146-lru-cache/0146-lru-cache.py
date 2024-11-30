class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()
    
    def get(self, key: int) -> int:
        # print("get", self.data, len(self.data), self.capacity)
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:      
        # print("put", self.data, len(self.data), self.capacity)

        self.data[key] = value
        self.data.move_to_end(key)

        # delete LRU item
        if len(self.data) > self.capacity:
            _ = self.data.popitem(False)
            




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)