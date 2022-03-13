import sys
import heapq


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    buses = [[] for _ in range(n)]
    for _ in range(m):
        f, t, c = map(int, sys.stdin.readline().split())
        buses[f - 1].append((t - 1, c))
    start, end = map(int, sys.stdin.readline().split())
    prio = []
    distances = [100000001 for _ in range(n)]
    distances[start - 1] = 0
    heapq.heappush(prio, (0, start - 1))
    while prio:
        dist, dest = heapq.heappop(prio)
        if dist > distances[dest]:
            continue
        for ndest, ndist in buses[dest]:
            cost = dist + ndist
            if cost < 100000001 and cost < distances[ndest]:
                heapq.heappush(prio, (cost, ndest))
                distances[ndest] = cost
    print(distances[end - 1])


main()
