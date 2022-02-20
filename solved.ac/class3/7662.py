import sys
import heapq


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        k = int(sys.stdin.readline())
        maxis = []
        minis = []
        count = 0
        ids = {}
        for _ in range(k):
            c, v = sys.stdin.readline().split()
            v = int(v)
            if c == "I":
                count += 1
                heapq.heappush(minis, v)
                heapq.heappush(maxis, -v)
                if v in ids:
                    ids[v] += 1
                else:
                    ids[v] = 1
            elif c == "D" and count > 0:
                count -= 1
                if v > 0:
                    while maxis:
                        maxi = -heapq.heappop(maxis)
                        if ids[maxi]:
                            ids[maxi] -= 1
                            break
                elif v < 0:
                    while minis:
                        mini = heapq.heappop(minis)
                        if ids[mini]:
                            ids[mini] -= 1
                            break
        if count == 0:
            print("EMPTY")
        else:
            maxi, mini = 0, 0
            while maxis:
                maxi = -heapq.heappop(maxis)
                if ids[maxi] > 0:
                    break
            while minis:
                mini = heapq.heappop(minis)
                if ids[mini] > 0:
                    break
            print(str(maxi) + " " + str(mini))


main()
