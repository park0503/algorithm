import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

suma = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    suma[i] = suma[i - 1] + numbers[i - 1]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    result = suma[b] - suma[a - 1]

    print(result)
