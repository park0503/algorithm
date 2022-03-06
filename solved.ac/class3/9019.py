import sys
from collections import deque

t = int(sys.stdin.readline())
results = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    stack = deque()
    visited = set()
    result = ""
    while a != b:
        d = a * 2 % 10000 if a * 2 > 9999 else a * 2
        s = 9999 if a == 0 else a - 1
        l = a % 1000 * 10 + a // 1000
        r = a % 10 * 1000 + a // 10
        if d not in visited:
            stack.append((d, result + "D"))
            visited.add(d)
        if s not in visited:
            stack.append((s, result + "S"))
            visited.add(s)
        if l not in visited:
            stack.append((l, result + "L"))
            visited.add(l)
        if r not in visited:
            stack.append((r, result + "R"))
            visited.add(r)
        if stack:
            temp = stack.popleft()
            a, result = temp[0], temp[1]
        else:
            break
    results.append(result)

for result in results:
    print(result)
