import sys


def main():
    n = int(sys.stdin.readline())
    house = []
    hori = [[0 for _ in range(n)] for _ in range(n)]
    verti = [[0 for _ in range(n)] for _ in range(n)]
    diag = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        house.append(list(map(int, sys.stdin.readline().split())))
    if house[n - 1][n - 1] > 0:
        print(0)
        return
    for i in range(1, n):
        if house[0][i] > 0:
            break
        hori[0][i] = 1
    for i in range(1, n):
        for j in range(1, n):
            if house[i][j] < 1:
                hori[i][j] = hori[i][j - 1] + diag[i][j - 1]
                verti[i][j] = verti[i - 1][j] + diag[i - 1][j]
                if house[i - 1][j] < 1 and house[i][j - 1] < 1:
                    diag[i][j] = hori[i - 1][j - 1] + \
                        verti[i - 1][j - 1] + diag[i - 1][j - 1]
    print(hori[n - 1][n - 1] + verti[n - 1][n - 1] + diag[n - 1][n - 1])


main()
