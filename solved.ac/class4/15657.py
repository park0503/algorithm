import sys
from itertools import combinations_with_replacement


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    results = list(combinations_with_replacement(arr, m))
    for result in results:
        for num in result:
            print(num, end=' ')
        print('')


main()
