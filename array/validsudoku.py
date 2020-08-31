board = [[".", ".", ".", ".", ".", ".", "5", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["9", "3", ".", ".", "2", ".", "4", ".", "."], [".", ".", "7", ".",
                                                                                                                                                                                                      ".", ".", "3", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "3", "4", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "."], [".", ".", ".", ".", ".", "5", "2", ".", "."]]
dictrows = {}
flag = 0
for i in range(9):
    setofrowvalues = set()
    for j in range(9):
        if board[i][j] != ".":
            if board[i][j] in setofrowvalues:
                flag = 1
                print("row")
                break
            else:
                setofrowvalues.add(board[i][j])

for i in range(9):
    setofrowvalues = set()
    for j in range(9):
        if board[j][i] != ".":
            if board[j][i] in setofrowvalues:
                flag = 1
                print("col")
                break
            else:
                setofrowvalues.add(board[j][i])
a, b, c, d = 0, 3, 0, 3
for i in range(9):
    setofrowvalues = set()
    for j in range(a, b):
        for k in range(c, d):
            if board[j][k] != ".":
                if board[j][k] in setofrowvalues:
                    flag = 1
                    print("box")
                    break
                else:
                    setofrowvalues.add(board[j][k])
    if i < 2:
        c = c+3
        d = d+3
        a = 0
        b = 3
    elif i == 2:
        c = 0
        d = 3
        a = 3
        b = 6
    elif i < 5:
        c = c+3
        d = d+3
    elif i == 5:
        c, d = 0, 3
        a, b = 6, 9
    elif i < 8:
        a, b = 6, 9
        c = c+3
        d = d+3
if flag == 0:
    print("true")
else:
    print("false")
for i in range(9):
    for j in range(9):
        print(board[i][j], end=" ")
    print()
