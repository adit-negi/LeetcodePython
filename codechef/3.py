t = int(input())
for i in range(t):
    p = str(input())

    def convert(p):
        if p[6:] == 'AM':
            if p[:2] == '12':
                p = int('00'+p[3:5])
            else:
                p = int(p[:2] + p[3:5])
        else:
            if p[:2] == '12':
                p = int(p[:2] + p[3:5])
            else:
                p = int(str(int(p[:2])+12) + p[3:5])
        return p
    p = convert(p)

    n = int(input())
    out = ""
    for j in range(n):
        string = str(input())
        s1 = string[0:8]
        s2 = string[9:]

        s1 = convert(s1)
        s2 = convert(s2)
        if s1 <= p <= s2:
            out += "1"
        else:
            out += "0"
    print(out)
