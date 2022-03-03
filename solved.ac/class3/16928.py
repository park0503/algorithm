import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    ladders = {}
    snakes = {}
    board = [0 for _ in range(101)]
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().split())
        ladders[start] = end
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())
        snakes[start] = end
    for i in range(2, 8):
        if i in snakes:
            board[i] = -1
            board[snakes[i]] = 1
        elif i in ladders:
            board[i] = -2
            board[ladders[i]] = 1
        else:
            board[i] = 1
    current = 8
    while current < 101:
        if board[current] == -1:
            current += 1
            continue
        temp = []
        if board[current] > 0:
            temp.append(board[current])
        for j in range(1, 7):
            if board[current - j] > 0:
                temp.append(board[current - j] + 1)
        board[current] = min(temp)
        if current in snakes:
            if not board[snakes[current]] or board[snakes[current]] > board[current]:
                board[snakes[current]] = board[current]
            board[current] = -1
            current = snakes[current]
            continue
        if current in ladders:
            if not board[ladders[current]] or board[ladders[current]] > board[current]:
                board[ladders[current]] = board[current]
            board[current] = -2
        current += 1
    print(board[100])


main()
