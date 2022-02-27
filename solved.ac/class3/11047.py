import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
    togo = k
    result = 0
    while togo:
        for i in range(n + 1):
            if i == n or coins[i] > togo:
                result += togo // coins[i - 1]
                togo %= coins[i - 1]
    print(result)


main()
