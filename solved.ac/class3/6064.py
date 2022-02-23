import sys

t = int(sys.stdin.readline())


def kaing(m, n, x, y):
    mr, nr = 0, 0
    cm, cn = 0, 0
    diff = abs(x - y)
    while (mr == 0 and cn == 0) or cm != cn:
        r = abs(cm - cn)
        if r == diff:
            if mr * m + x == nr * n + y:
                return mr * m + x
        if cm + m > cn + n:
            nr += 1
            cn += n
        else:
            mr += 1
            cm += m
    return -1


for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(kaing(m, n, x, y))
