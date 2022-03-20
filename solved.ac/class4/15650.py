import sys
from itertools import permutations


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = [i for i in range(1, n + 1)]
    results = permutations(arr, m)
    print(results)
