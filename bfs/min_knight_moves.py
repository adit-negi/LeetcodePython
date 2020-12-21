class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, -2), (2, -1), (2, 1), (1, 2),
                      (-1, 2), (-2, 1), (-2, -1), (-2, -2)]
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            res += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2

        def bfs():
            visited = set()
            q = [(0, 0, 0)]
            while q:
                i, j, dist = q.pop(0)
                visited.add((i, j))
                if i == x and j == y:
                    return dist+res
                for a, b in directions:
                    if (i+a, j+b) not in visited:
                        q.append((i+a, j+b, dist+1))

        return bfs()
