import sys


def main():
    n = int(sys.stdin.readline())
    tree = {}
    parents = {}
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        if a in tree:
            tree[a].append(b)
        else:
            tree[a] = [b]
        if b in tree:
            tree[b].append(a)
        else:
            tree[b] = [a]
    visited = [False for _ in range(n + 1)]
    stack = []
    stack.append(1)
    visited[1] = True
    while stack:
        c = stack.pop()
        if c not in tree:
            continue
        for next in tree[c]:
            if not visited[next]:
                visited[next] = True
                parents[next] = c
                stack.append(next)
    for i in range(2, n + 1):
        print(parents[i])


main()
