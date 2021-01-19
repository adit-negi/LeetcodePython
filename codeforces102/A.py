t = int(input())
for i in range(t):
    n, d = input().split()
    n, d = int(n), int(d)
    arr = list(map(int, input().split()))
    arr.sort()
    third_element = min(arr[0]+arr[1], arr[-1])

    if third_element <= d:
        print('YES')
    else:
        print('NO')
