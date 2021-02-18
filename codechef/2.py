t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x = arr.pop()
    y = arr.pop(0)
    m = 0
    for z in arr:
        print(x, y, z)
        m = max(abs(x-y) + abs(y-z)+abs(z-x), m)
    print(m)
