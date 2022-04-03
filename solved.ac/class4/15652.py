import sys
from itertools import combinations_with_replacement


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = [i for i in range(1, n + 1)]
    results = list(combinations_with_replacement(arr, m))
    for result in results:
        for num in result:
            print(num, end=' ')
        print('')


main()
