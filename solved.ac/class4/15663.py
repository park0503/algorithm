import sys
from itertools import permutations


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    results = sorted(set(permutations(arr, m)))
    for result in results:
        for num in result:
            print(num, end=' ')
        print('')


main()
