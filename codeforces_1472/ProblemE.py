t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    out = []
    for j in range(n):
        a, b = input().split()
        arr.append([int(a), int(b)])
    harr = arr.copy()
    warr = arr.copy()
    warr.sort(key=lambda x: x[1])
    harr.sort()
    d = {}
    for j in range(len(arr)):
        d[tuple(arr[j])] = j+1
    flag = False
    for j in range(len(arr)):
        cnt = 0
        flag = False
        while cnt < n:
            if arr[j][0] > harr[cnt][0] and arr[j][1] > harr[cnt][1]:
                out.append(d[tuple(harr[cnt])])
                flag = True
                break
            if arr[j][0] > warr[cnt][1] and arr[j][1] > warr[cnt][0]:
                out.append(d[tuple(warr[cnt])])
                flag = True
                break
            if arr[j][0] <= harr[cnt][0] and arr[j][0] <= warr[cnt][0]:
                out.append(-1)
                flag = True
                break
            cnt += 1
        if not flag:
            out.append(-1)
    print(*out)
