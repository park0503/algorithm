import sys


def main():
    n = int(sys.stdin.readline())
    choos = list(map(int, sys.stdin.readline().split()))
    ables = choos
    choos.sort()
    count = 2
    for i in range(n):
        for j in range(i, n):

    print(choos)


main()
