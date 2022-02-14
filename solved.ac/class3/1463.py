import sys
import heapq


def main():
    x = int(sys.stdin.readline())
    shortest = [0 for _ in range(x + 1)]
    for i in range(2, x + 1):
        temp = i
        candy = []
        if temp % 2 == 0:
            heapq.heappush(candy, shortest[temp // 2] + 1)
        if temp % 3 == 0:
            heapq.heappush(candy, shortest[temp // 3] + 1)
        heapq.heappush(candy, shortest[temp - 1] + 1)
        shortest[i] += candy[0]
    print(shortest[x])


main()
