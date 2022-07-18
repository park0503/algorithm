import sys
import heapq
import copy


def dijkstra(start, timetable, distances, paths):
    prio = []
    heapq.heappush(prio, [0, start, [start]])
    while prio:
        dist, dest, path = heapq.heappop(prio)
        if distances[dest - 1] < dist:
            continue
        distances[dest - 1] = dist
        for ndest, ndist in timetable[dest - 1].items():
            cost = dist + ndist
            if cost < distances[ndest - 1]:
                distances[ndest - 1] = cost
                npath = copy.deepcopy(path)
                npath.append(ndest)
                paths[ndest - 1] = npath
                heapq.heappush(prio, [cost, ndest, npath])


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    INF = n * 100000 + 1
    timetable = [{} for _ in range(n)]
    distances = [INF for _ in range(n)]
    paths = [[] for _ in range(n)]
    for _ in range(m):
        start, dest, cost = map(int, sys.stdin.readline().split())
        if dest in timetable[start - 1] and timetable[start - 1][dest] < cost:
            continue
        timetable[start - 1][dest] = cost
    start, end = map(int, sys.stdin.readline().split())
    dijkstra(start, timetable, distances, paths)
    print(distances[end - 1])
    print(len(paths[end - 1]))
    print(' '.join(map(str, paths[end - 1])))


main()
