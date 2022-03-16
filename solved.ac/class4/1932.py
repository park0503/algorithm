import sys


def main():
    n = int(sys.stdin.readline())
    tri = []
    for _ in range(n):
        tri.append(list(map(int, sys.stdin.readline().split())))
    dp = []
    dp.append(tri[0])
    for i in range(n - 1):
        temp = []
        temp.append(dp[i][0] + tri[i + 1][0])
        for j in range(1, i + 1):
            temp.append(max(dp[i][j - 1] + tri[i + 1]
                        [j], dp[i][j] + tri[i + 1][j]))
        temp.append(dp[i][-1] + tri[i + 1][-1])
        dp.append(temp)
    print(max(dp[n - 1]))


main()
