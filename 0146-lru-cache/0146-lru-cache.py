class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.data = {}
    
    def add(self, key: int, value: int) -> None:
        # add new item
        newItem = [key, value]
        self.data[key] = newItem
        self.queue.append(newItem)
        

    def remove(self, key: int) -> int:
        # remove the previous item
        item = self.data[key]
        value = item[1]
        del self.data[key]
        item[1] = None # deal with the dangling item in queue

        return value

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
            
        value = self.remove(key)
        self.add(key, value)

        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.remove(key)
        
        # delete LRU item
        if len(self.data.keys()) == self.capacity:
            item = self.queue.popleft()
            while item[1] == None:
                item = self.queue.popleft()
            self.remove(item[0])
        
        self.add(key, value)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)