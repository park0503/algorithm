import sys
from itertools import permutations


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    results = list(permutations(arr, m))
    for result in results:
        for num in result:
            print(num, end=' ')
        print('')


main()