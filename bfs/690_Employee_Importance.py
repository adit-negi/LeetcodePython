# question link - https://leetcode.com/problems/employee-importance/


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        g = defaultdict(list)
        for i in employees:
            g[i.id].append(i.importance)
            g[i.id].append(i.subordinates)
        s = 0

        def dfs(id):
            nonlocal s
            s += g[id][0]
            if g[id][1] != []:
                for i in g[id][1]:
                    dfs(i)
        dfs(id)
        return s
