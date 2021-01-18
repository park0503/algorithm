import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
product = a * b
while b != 0:
    a, b = b, a % b
print(a)
print(int(product / a))
