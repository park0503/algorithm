import sys

n, m = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(n + 1)]

dp[0] = 1
for i in range(1, n + 1):
    dp[i] = dp[i - 1] * i
print(dp[n]//dp[n - m]//dp[m])
