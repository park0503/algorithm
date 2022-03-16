import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n)]
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a - 1].append((b - 1, c))
    tree[b - 1].append((a - 1, c))

visited = [False for _ in range(n)]
first, result = -1, -1


def dfs(n, c):
    visited[n] = True
    if c > result:
        result = c
        first = n
    for dest, dist in tree[n]:
        if not visited[dest]:
            dfs(dest, c + dist)


dfs(0, 0)

visited = [False for _ in range(n)]
result = 0

dfs(first, 0)

print(result)
