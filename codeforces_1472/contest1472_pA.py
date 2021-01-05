t = int(input())
for i in range(t):
    w, h, n = input().split()
    w, h, n = int(w), int(h), int(n)
    area = w*h
    total = 1
    times = 1
    flag = False
    if n == 1:
        print('YES')
        flag = True
        continue
    while area % 2 == 0:
        total += times
        times *= 2
        area = area//2
        if total >= n:
            if not flag:
                flag = True
                print('YES')

    if not flag:
        print('NO')
