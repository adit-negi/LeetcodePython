count = {}
s = "dddccdbba"
for i in range(len(s)):
    if s[i] not in count:
        count[s[i]] = 1
    else:
        count[s[i]] = count[s[i]]+1
print(count)
