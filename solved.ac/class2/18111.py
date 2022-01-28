import sys


def main():
    n, m, b = map(int, sys.stdin.readline().split())
    ground = []
    for i in range(n):
        ground += list(map(int, sys.stdin.readline().split()))
    times = []
    for i in range(256, -1, -1):
        time = 0
        tempB = b
        for block in ground:
            diff = i - block
            if diff < 0:
                # 파내는 것들
                time -= 2 * diff
            elif diff > 0:
                # 채우는 것들
                time += diff
            tempB -= diff
        if tempB >= 0:
            temp = (time, i)
            times.append(temp)
    times.sort(key=lambda x: (x[0], -x[1]))
    print("%d %d" % (times[0][0], times[0][1]))


main()
