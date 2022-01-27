import sys


def main():
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        points.append(temp)
    points.sort(key=lambda x: (x[1], x[0]))
    for point in points:
        print("%d %d" % (point[0], point[1]))


main()
