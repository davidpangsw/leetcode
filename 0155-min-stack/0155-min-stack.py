class MinStack:
    mins = []
    data = []
    def __init__(self):
        self.mins = []
        self.data = []
        
    def push(self, val: int) -> None:
        curMin = self.mins[-1] if self.mins else float("inf")
        self.mins.append(min(curMin, val))
        self.data.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()