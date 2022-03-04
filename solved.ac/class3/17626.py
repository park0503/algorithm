import sys


def main():
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    power = [0]
    maxi = 1
    while maxi ** 2 <= n:
        power.append(maxi ** 2)
        maxi += 1
    power.append(maxi ** 2)
    for j in range(2, n + 1):
        i = 1
        smallest = 5
        while j > power[i]:
            candy = dp[j - power[i]] + 1
            if candy < smallest:
                smallest = candy
            i += 1
        if power[i] == j:
            dp[j] = 1
            continue
        dp[j] = smallest
    print(dp[n])


main()
