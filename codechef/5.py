from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(str, input().split()))
    ans = 0
    ans_set = defaultdict(list)
    for i in l:
        stripped = i[1:]
        ans_set[stripped].append(i[0])
    stripped_list = list(ans_set.keys())
    for i in range(len(ans_set)):
        for j in range(i+1, len(ans_set)):
            add = len(set(ans_set[stripped_list[i]]+ans_set[stripped_list[j]]))
            ans += (add-len(ans_set[stripped_list[i]])) * \
                (add-len(ans_set[stripped_list[j]]))
    print(ans*2)
