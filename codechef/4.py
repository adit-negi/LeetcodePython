t = int(input())
for i in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    l = list(map(int, input().split()))
    d = {}
    indexes = {}
    temp = w.copy()
    for i in range(len(w)):
        d[w[i]] = l[i]
    for i in range(len(w)):
        indexes[w[i]] = i
    temp.sort()
    taps = 0
    for i in range(len(temp)):
        if i == 0:
            continue
        li = indexes[temp[i-1]]
        ci = indexes[temp[i]]
        if ci > li:
            continue
        jump = d[temp[i]]
        curr_taps = (li - ci)//jump + 1
        taps += curr_taps
        indexes[temp[i]] = indexes[temp[i]] + curr_taps*jump
    print('taps', taps)
