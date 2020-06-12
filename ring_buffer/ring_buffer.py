class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.values = {}
    def append(self, item):
        self.counter += 1
        if self.counter >= self.capacity:
            self.counter = 0
        self.values[f"{self.counter}"] = item
    def get(self):
        result = []
        for value in self.values.values():
            result.append(value)
        return result