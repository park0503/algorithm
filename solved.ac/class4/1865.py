import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    edges = []
    for i in range(m + w):
        s, e, t = map(int, sys.stdin.readline().split())
        if i > m - 1:
            t *= -1
        else:
            edges.append((e - 1, s - 1, t))
        edges.append((s - 1, e - 1, t))
    distances = [0 for _ in range(n)]
    result = False
    for i in range(n):
        for src, dest, dist in edges:
            if distances[src] < 5000001 and distances[src] + dist < distances[dest]:
                if i == n - 1:
                    result = True
                    break
                distances[dest] = distances[src] + dist
    if result:
        print("YES")
    else:
        print("NO")
