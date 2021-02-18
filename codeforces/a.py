t = int(input())
for i in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    flag = True
    for i in range(n-1):
        h[i+1] = h[i]-i+h[i+1]
        if h[i+1] <= i:
            flag = False
            print('NO')
            break
        h[i] = i
    if flag:
        for i in range(n-1):
            if h[i+1] > h[i]:
                pass
            else:
                print('NO')
                flag = False
                break
        if flag:
            print('YES')
