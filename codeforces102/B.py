t = int(input())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


for i in range(t):
    a = str(input())
    b = str(input())
    if set(list(a)) == set(list(b)) and len(set(list(a))) == 1:
        a = list(a)
        x = len(a)
        temp = len(set(a))
        a = a[0:temp]
        print("".join(list(a)) *
              (int(lcm(x, len(b))//temp)))
        continue
    if len(a) > len(b):
        x, y = len((list(a))), len((list(b)))
        if set(list(a)) == set(list(b)) and b*(int(lcm(x, y)//len(b))) == a*(int(lcm(x, y)//len(a))):
            print(a*(int(lcm(x, y)//len(a))))
            continue
    elif len(b) > len(a):
        x, y = len((list(a))), len((list(b)))
        if set(list(a)) == set(list(b)) and b*(int(lcm(x, y)//len(b))) == a*(int(lcm(x, y)//len(a))):
            print(a*(int(lcm(x, y)//len(a))))
            continue
    if len(a) == len(b):
        if a == b:
            print(a)
            continue
    print(-1)
