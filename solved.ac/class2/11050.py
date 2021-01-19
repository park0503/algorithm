import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
result = 1
son = 1
mother = 1
for i in range(k):
    son *= n
    mother *= (i + 1)
    n -= 1
result = int(son / mother)
print(result)
