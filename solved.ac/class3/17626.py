import sys


def main():
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for j in range(2, n + 1):
        i = 1
        smallest = 5
        while j > i ** 2:
            candy = dp[j - i ** 2] + 1
            if candy < smallest:
                smallest = candy
            i += 1
        if i ** 2 == j:
            dp[j] = 1
            continue
        dp[j] = smallest
    print(dp[n])


main()
