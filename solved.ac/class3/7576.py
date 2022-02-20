import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    tomatos = []
    stack = deque()
    riped = 0
    unriped = 0
    day = 0
    for _ in range(m):
        tomatos.append(list(map(int, sys.stdin.readline().split())))
    for i in range(m):
        for j in range(n):
            if tomatos[i][j] == 0:
                unriped += 1
            elif tomatos[i][j] == 1:
                tomatos[i][j] = 2
                riped += 1
                stack.append((i, j))
    while unriped > 0:
        new = 0
        day += 1
        for _ in range(riped):
            t = stack.popleft()
            i, j = t[0], t[1]
            if i > 0 and tomatos[i - 1][j] == 0:
                tomatos[i - 1][j] = 2
                stack.append((i - 1, j))
                new += 1
                unriped -= 1
            if j > 0 and tomatos[i][j - 1] == 0:
                tomatos[i][j - 1] = 2
                stack.append((i, j - 1))
                new += 1
                unriped -= 1
            if i < m - 1 and tomatos[i + 1][j] == 0:
                tomatos[i + 1][j] = 2
                stack.append((i + 1, j))
                new += 1
                unriped -= 1
            if j < n - 1 and tomatos[i][j + 1] == 0:
                tomatos[i][j + 1] = 2
                stack.append((i, j + 1))
                new += 1
                unriped -= 1
        if new == 0:
            day = -1
            break
        else:
            riped = new
    print(day)
    return


main()
