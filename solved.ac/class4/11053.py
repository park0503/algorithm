import sys


def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(max(A) + 1)]
    dp[A[0]] = 1
    for i in range(1, N):
        maxi = 0
        for j in range(0, A[i]):
            if dp[j] > maxi:
                maxi = dp[j]
        dp[A[i]] = maxi + 1
    print(max(dp))


main()
