import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    floor = n % h
    if floor == 0:
        floor = h
        ho = int(n / h)
    else:
        ho = int(n / h) + 1
    room = 100 * floor + ho
    print(room)
