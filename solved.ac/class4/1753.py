import sys
import heapq


def main():
    V, E = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u - 1].append((v - 1, w))
    prio = []
    distances = [200001 for _ in range(V)]
    distances[k - 1] = 0
    heapq.heappush(prio, (0, k - 1))
    while prio:
        dist, dest = heapq.heappop(prio)
        if dist > distances[dest]:
            continue
        for ndest, ndist in graph[dest]:
            cost = dist + ndist
            if cost < distances[ndest]:
                distances[ndest] = cost
                heapq.heappush(prio, (cost, ndest))
    for distance in distances:
        if distance > 200000:
            print("INF")
        else:
            print(distance)


main()
