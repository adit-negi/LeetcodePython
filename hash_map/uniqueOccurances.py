class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = dict(Counter(arr))
        l = list(c.values())
        return len(l) == len(set(l))
