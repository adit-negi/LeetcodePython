t = int(input())
for i in range(t):
    n = int(input())
    xc = []
    yc = []
    for j in range(n):
        x, y = input().split()
        xc.append(int(x))
        yc.append(int(y))
    xc.sort()
    yc.sort()
    lm = (n)//2
    rm = (n-1)//2
    print((abs(xc[rm]-xc[lm])+1)*(abs(yc[rm]-yc[lm])+1))
