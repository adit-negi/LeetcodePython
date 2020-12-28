class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.m = size
        self.q = []

    def next(self, val: int) -> float:
        if len(self.q) < self.m:
            self.q.append(val)
            return sum(self.q)/len(self.q)
        else:
            self.q.pop(0)
            self.q.append(val)
            return sum(self.q)/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.m = size
        self.q = []

    def next(self, val: int) -> float:
        if len(self.q) < self.m:
            self.q.append(val)
            return sum(self.q)/len(self.q)
        else:
            self.q.pop(0)
            self.q.append(val)
            return sum(self.q)/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
