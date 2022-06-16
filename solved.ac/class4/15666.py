import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
inp = list(set(map(int, sys.stdin.readline().split())))
inp.sort()
for comb in combinations_with_replacement(inp, m):
    for el in comb:
        print(el, end=" ")
    print()
