import sys


def main():
    n = int(input())
    conferences = []
    count = 0
    ableTime = 0
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().split())
        conferences.append([start, end])
    conferences.sort(key=lambda x: (x[1], x[0]))
    for conference in conferences:
        if conference[0] >= ableTime:
            ableTime = conference[1]
            count += 1
    print(count)


main()
