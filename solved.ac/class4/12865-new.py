import sys

n, k = map(int, sys.stdin.readline().split())
things = []
dp = [0 for _ in range(k + 1)]
for _ in range(n):
    things.append(list(map(int, sys.stdin.readline().split())))
for thing in things:
    w, v = thing[0], thing[1]
    for i in range(k - w, -1, -1):
        if i == 0 or dp[i] > 0:
            dp[i + w] = max(dp[i + w], dp[i] + v)
print(max(dp))
