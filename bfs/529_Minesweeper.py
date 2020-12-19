# question link - https://leetcode.com/problems/minesweeper/


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0),
                      (0, -1), (-1, -1), (-1, 1), (1, -1)]
        n, m = len(board), len(board[0])

        def recursive(board, row, col, visited):
            mines = 0
            if board[row][col] == 'M' or board[row][col] == 'E':
                if board[row][col] == 'M':
                    board[row][col] = 'X'
                    return board
                elif board[row][col] == "E":
                    l = []
                    mines = 0
                    for i, j in directions:
                        r, c = row+i, col+j
                        if (r, c) and 0 <= r < n and 0 <= c < m:
                            if board[r][c] == "M" or board[r][c] == "X":
                                mines += 1
                            if board[r][c] == "M" or board[r][c] == "E":
                                l.append((r, c))
                    if mines == 0:
                        board[row][col] = 'B'
                        for i, j in l:
                            recursive(board, i, j, visited)
                    else:
                        board[row][col] = str(mines)

            return board
        return recursive(board, click[0], click[1], set())
