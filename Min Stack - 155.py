class MinStack:

    def __init__(self):
        self.stack = {}
        self.add_count = 0
        self.del_count = 0
        self.min_element = []
        
    def push(self, val: int) -> None:
        self.stack[self.add_count] = val
        if self.min_element == [] or val <= self.min_element[-1]:
            self.min_element.append(val)
        self.add_count += 1
        
    def pop(self) -> None:
        save = self.stack.pop(self.add_count - 1)
        if save == self.min_element[-1]:
            self.min_element.pop()
        self.add_count -= 1
        
    def top(self) -> int:
        if self.add_count >= 0:
            return self.stack[self.add_count-1]
        
    def getMin(self) -> int:
        return self.min_element[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()