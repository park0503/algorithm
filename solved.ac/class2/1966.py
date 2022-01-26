import sys
from collections import deque
def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n, m = map(int, sys.stdin.readline())
        qu = list(map(int, sys.stdin.readline()))
        out = 0
        while n:
            maxi = max(qu)
            current = qu.pop(0)
            if maxi > current:
                qu.append(current)
            else:
                out += 1
                n -= 1
                if m == 0:
                    break
            m = m - 1 if m > 0 else n - 1