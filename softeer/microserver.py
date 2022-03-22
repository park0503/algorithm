import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    mss = deque(map(int, sys.stdin.readline()))
    mss.sort()


main()
