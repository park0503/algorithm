import sys


def main():
    n = int(sys.stdin.readline())
    tri = []
    for _ in range(n):
        tri.append(list(map(int, sys.stdin.readline().split())))
    dp = []
    dp[0] = tri[0]
    for i in range(1, n - 1):
        temp = []
        for j in range(i):
            temp.append(min(tri[i - 1][j], tri[i - 1][j + 1]))
        dp[i].append(temp)
    print(dp)


main()
