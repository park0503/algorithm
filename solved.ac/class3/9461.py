import sys

t = int(sys.stdin.readline())

p = [0 for _ in range(101)]
p[0] = 0
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
next = 5


for _ in range(t):
    n = int(sys.stdin.readline())
    if n < next:
        print(p[n])
    else:
        for i in range(next, n + 1):
            p[i] = p[i - 1] + p[i - 5]
        next = n + 1
        print(p[n])
