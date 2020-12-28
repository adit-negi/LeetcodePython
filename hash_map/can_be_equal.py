class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1 = dict(Counter(target))
        c2 = dict(Counter(arr))
        if len(target) != len(arr):
            return False
        for i in c1:
            if i not in c2:
                return False
            if c1[i] != c2[i]:
                return False
        return True
