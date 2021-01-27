import sys
sys.setrecursionlimit(10000)

t = int(sys.stdin.readline().rstrip())


def chain(row, column, max_row, max_column):
    cabbage[row][column] = 2
    if column > 0 and cabbage[row][column - 1] == 1:
        chain(row, column - 1, max_row, max_column)
    if row > 0 and cabbage[row - 1][column] == 1:
        chain(row - 1, column, max_row, max_column)
    if column < max_column - 1 and cabbage[row][column + 1] == 1:
        chain(row, column + 1, max_row, max_column)
    if row < max_row - 1 and cabbage[row + 1][column] == 1:
        chain(row + 1, column, max_row, max_column)


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    cabbage = [[0] * m for _ in range(n)]
    worm = 0
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        cabbage[b][a] = 1
    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                chain(i, j, n, m)
                worm += 1
    print(worm)
