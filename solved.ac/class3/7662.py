import sys
import heapq


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        k = int(sys.stdin.readline())
        maxis = []
        minis = []
        count = 0
        for _ in range(k):
            c, v = sys.stdin.readline().split()
            v = int(v)
            if c == "I":
                count += 1
                heapq.heappush(minis, v)
                heapq.heappush(maxis, -v)
            elif c == "D" and count > 0:
                count -= 1
                if v == 1:
                    heapq.heappop(maxis)
                elif v == -1:
                    heapq.heappop(minis)
                if count == 0:
                    maxis = []
                    minis = []
        if count == 0:
            print("EMPTY")
        else:
            print(str(-heapq.heappop(maxis)) + " " + str(heapq.heappop(minis)))


main()
