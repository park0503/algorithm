import sys


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    cities = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if cities[a - 1][b - 1] == 0 or cities[a - 1][b - 1] > c:
            cities[a - 1][b - 1] = c
    for k in range(n):
        for i in range(n):
            if cities[i][k] == 0:
                continue
            for j in range(n):
                if cities[k][j] == 0 or i == j:
                    continue
                if cities[i][j] == 0 or cities[i][k] + cities[k][j] < cities[i][j]:
                    cities[i][j] = cities[i][k] + cities[k][j]
    for row in cities:
        for el in row:
            print(el, end=" ")
        print("")


main()
