import sys
from collections import deque

t = int(sys.stdin.readline())


for _ in range(t):
    f = deque(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    if n > 0:
        a = sys.stdin.readline().strip()
        a = deque(map(int, a[1:-1].split(',')))
    else:
        sys.stdin.readline()
        a = deque()
    r = False
    e = False
    for c in f:
        if c == "R":
            r = not r
        elif c == "D":
            if a:
                if r:
                    a.pop()
                else:
                    a.popleft()
            else:
                e = True
                break
    if e:
        print("error")
        continue
    if r:
        a.reverse()
    result = ""
    for num in a:
        result += str(num) + ","
    result = "[" + result[:-1] + "]"
    print(result)
