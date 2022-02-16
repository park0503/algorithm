import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    dj = {}
    dbj = []
    for _ in range(n):
        dj[sys.stdin.readline().strip()] = True
    for _ in range(m):
        nom = sys.stdin.readline().strip()
        if nom in dj:
            dbj.append(nom)
    dbj.sort()
    print(len(dbj))
    for nom in dbj:
        print(nom)


main()
