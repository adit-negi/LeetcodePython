from functools import lru_cache
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    visited = set()
    m = 0
    for j in range(n):
        s = 0
        index = j
        if index not in visited:
            while index < n:
                visited.add(index)
                s += a[index]
                index += a[index]
                if index in visited:
                    break
        m = max(s, m)
    print(m)
