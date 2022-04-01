import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    things = []
    for _ in range(n):
        things.append(list(map(int, sys.stdin.readline().split())))
    for i in range(things[0][0], k + 1):
        dp[0][i] = things[0][1]
    for i in range(1, n):
        for j in range(1, k + 1):
            if things[i][0] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                               [j - things[i][0]] + things[i][1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n - 1][k])


main()
