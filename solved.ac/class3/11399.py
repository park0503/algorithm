import sys

def main():
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n)]
    people = list(map(int, sys.stdin.readline().split()))
    people.sort()
    dp[0] = people[0]
    for i in range(1, n):
        dp[i] = dp[i - 1] + people[i]
    print(sum(dp))

main()