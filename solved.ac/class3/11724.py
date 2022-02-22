import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    visited = [False for _ in range(n)]
    result = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    while True:
        stack = []
        current = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                current = i + 1
                break
        if current == 0:
            break
        while True:
            find = False
            for node in graph[current]:
                if not visited[node - 1]:
                    visited[node - 1] = True
                    stack.append(current)
                    current = node
                    find = True
                    break
            if find:
                continue
            if stack:
                current = stack.pop()
            else:
                break
        result += 1
    print(result)


main()
