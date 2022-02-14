import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    poketmons = {}
    dogam = []
    for i in range(n):
        poketmon = sys.stdin.readline()
        poketmons[poketmon] = i
        dogam.append(poketmon)
    for i in range(m):
        problem = sys.stdin.readline()
        if ord(problem[0]) < 58:
            print(dogam[int(problem) - 1][:-1])
        else:
            print(poketmons[problem] + 1)


main()
