# question link - https://leetcode.com/problems/walls-and-gates/

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms != []:

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            n, m = len(rooms), len(rooms[0])

            def bfs(i, j):
                q = [(i, j, 0)]
                INF = 2147483647
                visited = set()
                visited.add((i, j))
                while q:
                    row, col, curr = q.pop(0)
                    for a, b in directions:
                        r = a+row
                        c = b+col
                        if 0 <= r < n and 0 <= c < m and rooms[r][c] != -1 and rooms[r][c] != 0 and (r, c) not in visited:
                            visited.add((r, c))
                            q.append((r, c, curr+1))
                            rooms[r][c] = min(rooms[r][c], curr+1)
                return

            for i in range(n):
                for j in range(m):
                    if rooms[i][j] == 0:
                        bfs(i, j)
