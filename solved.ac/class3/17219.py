import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    memo = {}
    result = []
    for _ in range(n):
        mail, pwd = sys.stdin.readline().split()
        memo[mail] = pwd
    for _ in range(m):
        q = sys.stdin.readline().strip()
        result.append(memo[q])
    for r in result:
        print(r)


main()
