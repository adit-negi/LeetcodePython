class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        up = [[0 for _ in range(C)] for _ in range(R)]
        down = [[0 for _ in range(C)] for _ in range(R)]
        left = [[0 for _ in range(C)] for _ in range(R)]
        right = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if r == 0:
                    up[r][c] = grid[r][c]
                else:
                    up[r][c] = grid[r][c] + up[r-1][c] if grid[r][c] == 1 else 0

        for r in range(R-1, -1, -1):
            for c in range(C):
                if r == R-1:
                    down[r][c] = grid[r][c]
                else:
                    down[r][c] = grid[r][c] + \
                        down[r+1][c] if grid[r][c] == 1 else 0

        for c in range(C):
            for r in range(R):
                if c == 0:
                    left[r][c] = grid[r][c]
                else:
                    left[r][c] = grid[r][c] + \
                        left[r][c-1] if grid[r][c] == 1 else 0

        for c in range(C-1, -1, -1):
            for r in range(R):
                if c == C-1:
                    right[r][c] = grid[r][c]
                else:
                    right[r][c] = grid[r][c] + \
                        right[r][c+1] if grid[r][c] == 1 else 0

        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                side = min(up[r][c], left[r][c])
                for i in range(side-1, -1, -1):
                    if i < res:
                        break
                    if min(down[r-i][c-i], right[r-i][c-i]) >= i + 1:
                        res = max(res, i + 1)
                        break
        return res * res
