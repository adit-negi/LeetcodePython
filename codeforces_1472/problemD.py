t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even = []
    odd = []

    alice = 0
    bob = 0
    a.sort()
    flag = True
    while a:
        temp = a.pop()
        if flag:

            if temp % 2 == 0:
                alice += temp
            flag = False
        else:
            if temp % 2 == 1:
                alice -= temp
            flag = True

    if alice > 0:
        print("Alice")
    elif 0 > alice:
        print('Bob')
    else:
        print('Tie')
