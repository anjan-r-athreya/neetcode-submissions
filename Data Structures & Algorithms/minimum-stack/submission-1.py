class MinStack:

    def __init__(self):
        self.items = []
        self.min_element = float('inf')
        self.minarray = [self.min_element]
        
    def push(self, val: int) -> None:
        self.items.append(val)
        if val < self.min_element:
            self.min_element = val
            self.minarray.append(val)

    def pop(self) -> None:
        if len(self.items) > 0:
            if self.items[-1] == self.min_element:
                self.minarray.pop()
            self.items.pop()

    def top(self) -> int:
        if len(self.items) > 0:
            return self.items[-1]

    def getMin(self) -> int:
        return self.minarray[-1]
        