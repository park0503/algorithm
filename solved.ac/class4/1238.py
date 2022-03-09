import sys
import heapq


def main():
    n, m, x = map(int, sys.stdin.readline().split())
    roads = [[] for _ in range(n)]
    for _ in range(m):
        f, t, c = map(int, sys.stdin.readline().split())
        roads[f - 1].append((t - 1, c))
    dtox = [0 for _ in range(n)]
    for i in range(n):
        prio = []
        d = [100001 for _ in range(n)]
        d[i] = 0
        heapq.heappush(prio, (0, i))
        while prio:
            c, t = heapq.heappop(prio)
            if d[t] < c:
                continue
            for nt, nc in roads[t]:
                cost = c + nc
                if cost < d[nt]:
                    d[nt] = cost
                    heapq.heappush(prio, (cost, nt))
        if i == x - 1:
            for i in range(n):
                dtox[i] += d[i]
        else:
            dtox[i] += d[x - 1]
    print(max(dtox))


main()
