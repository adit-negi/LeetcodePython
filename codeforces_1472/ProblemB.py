t = int(input())
for i in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    s = sum(candies)
    if s % 2 != 0:
        print('NO')
        continue

    temp = s//2
    if temp % 2 != 0:
        if candies.count(1) > 0:
            print('YES')
            continue
        else:
            print('NO')
            continue

    print('YES')
