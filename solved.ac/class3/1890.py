import sys


def main():
    n = int(sys.stdin.readline())
    counts = [[0 for _ in range(n)] for _ in range(n)]
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    counts[0][0] += 1
    for i in range(n):
        for j in range(n):
            number = board[i][j]
            if number == 0:
                continue
            if i + number < n:
                counts[i + number][j] += counts[i][j]
            if j + number < n:
                counts[i][j + number] += counts[i][j]
    print(counts[n-1][n-1])


main()
