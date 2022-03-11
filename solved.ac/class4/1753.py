import sys
import heapq


def main():
    v, e = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u - 1].append((v - 1, w))
    print(graph)
    prio = []
    distances = [200001 for _ in range(v)]
    print(distances)
    distances[k - 1] = 0
    heapq.heappush(prio, (0, k - 1))
    while prio:
        dist, dest = heapq.heappop(prio)
        if dist > distances[dest]:
            continue
        for ndest, ndist in graph[dest]:
            cost = dist + ndist
            if cost < distances[dest]:
                distances[dest] = cost
                heapq.heappush(prio, (cost, ndest))
    for distance in distances:
        if distance > 200000:
            print("INF")
        else:
            print(distance)


main()
