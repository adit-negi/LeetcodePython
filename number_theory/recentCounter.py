class RecentCounter:

    def __init__(self):
        self.counter = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.counter.append(t)
        cnt = 0
        for i in range(self.start, len(self.counter)):
            if t-3000 <= self.counter[i] <= t:
                cnt += 1
            elif self.counter[i] < t-3000:
                self.start = i+1
        return cnt


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
