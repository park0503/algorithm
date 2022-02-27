import sys
import heapq


def main():
    n = int(sys.stdin.readline())
    a = []
    result = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x == 0:
            if not a:
                result.append(0)
            else:
                temp = heapq.heappop(a)
                result.append(temp[0] * temp[1])
        else:
            if x > 0:
                a.append((x, 1))
            elif x < 0:
                a.append((abs(x), -1))
    for el in result:
        print(el)


main()
