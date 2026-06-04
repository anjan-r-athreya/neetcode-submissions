class MinStack:

    def __init__(self):
        self.items = []
        
    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        if len(self.items) > 0:
            self.items.pop()

    def top(self) -> int:
        if len(self.items) > 0:
            return self.items[-1]

    def getMin(self) -> int:
        min_element = float('inf')
        for i in range(len(self.items)):
            if self.items[i] < min_element:
                min_element = self.items[i]
        return min_element
