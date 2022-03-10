import sys
import heapq

n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
v1, v2 = map(int, sys.stdin.readline().split())
prio = []
distances = [1600001 for _ in range(n)]
results = [0, 0]


def dijkstra(c):
    heapq.heappush(prio, (0, c))
    distances[c] = 0
    while prio:
        dist, dest = heapq.heappop(prio)
        if distances[dest] < dist:
            continue
        for ndest, ndist in graph[dest]:
            cost = dist + ndist
            if cost < distances[ndest]:
                distances[ndest] = cost
                heapq.heappush(prio, (cost, ndest))


case = [[0, v1 - 1, v2 - 1, n - 1], [0, v2 - 1, v1 - 1, n - 1]]
able = True

for i in range(2):
    for j in range(3):
        dijkstra(case[i][j])
        if distances[case[i][j + 1]] > 1600000:
            able = False
            break
        results[i] += distances[case[i][j + 1]]
        distances = [1600001 for _ in range(n)]
    if not able:
        break

if able:
    print(min(results))
else:
    print(-1)
