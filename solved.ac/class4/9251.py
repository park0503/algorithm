import sys


def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    n = len(a)
    m = len(b)
    board = [[0 if j == 0 or i == 0 else None for j in range(
        m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                board[i + 1][j + 1] = board[i][j] + 1
            else:
                board[i + 1][j + 1] = max(board[i + 1][j], board[i][j + 1])
    print(board[n][m])


main()
