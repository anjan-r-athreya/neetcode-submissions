class MinStack:

    def __init__(self):
        self.items = []
        self.min_element = float('inf')
        self.minarray = [self.min_element]
        
    def push(self, val: int) -> None:
        self.items.append(val)

        if not self.minarray:
            self.min_element = val
        else:
            self.min_element = min(val, self.min_element)
        self.minarray.append(self.min_element)

    def pop(self) -> None:
        if len(self.items) > 0:
            self.minarray.pop()
            self.items.pop()

            if len(self.minarray) > 0:
                self.min_element = self.minarray[-1]
            else:
                self.min_element = None

    def top(self) -> int:
        if len(self.items) > 0:
            return self.items[-1]

    def getMin(self) -> int:
        return self.min_element
        