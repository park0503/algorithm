from atexit import register
import sys

t = int(sys.stdin.readline())


def dslr(a, b):
    register = list(a)
    n = int(a)
    result = ""


for _ in range(t):
    a, b = sys.stdin.readline().split()
    print(dslr(a, b))
