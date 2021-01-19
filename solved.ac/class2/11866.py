import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
remain = deque([i for i in range(1, n+1)])
current = -1
result = []
for _ in range(n):
    current += k
    if current + 1 > len(remain):
        current %= len(remain)
    result.append(remain[current])
    del remain[current]
    current -= 1
print(f"<{result[0]}", end="")
for i in range(1, len(result)):
    print(f", {result[i]}", end="")
print(">")
