class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            if i % 2 == 1:
                odd += 1
        return min(even, odd)
