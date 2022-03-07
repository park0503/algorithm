import sys


a, b, c = map(int, sys.stdin.readline().split())


def power(n):
    if n == 1:
        return a % c
    result = power(n//2)
    if n % 2 == 1:
        return result * result * a % c
    else:
        return result * result % c


print(power(b))
