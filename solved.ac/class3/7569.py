import sys
from collections import deque


def main():
    n, m, h = map(int, sys.stdin.readline().split())
    tomatos = []
    stack = deque()
    riped = 0
    unriped = 0
    day = 0
    for _ in range(m):
        tomatos.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomatos[i][j][k] == 0:
                    unriped += 1
                elif tomatos[i][j][k] == 1:
                    tomatos[i][j][k] = 2
                    riped += 1
                    stack.append((i, j, k))
    while unriped > 0:
        new = 0
        day += 1
        for _ in range(riped):
            t = stack.popleft()
            i, j, k = t[0], t[1], t[2]
            if i > 0 and tomatos[i - 1][j][k] == 0:
                tomatos[i - 1][j][k] = 2
                stack.append((i - 1, j, k))
                new += 1
                unriped -= 1
            if j > 0 and tomatos[i][j - 1][k] == 0:
                tomatos[i][j - 1][k] = 2
                stack.append((i, j - 1, k))
                new += 1
                unriped -= 1
            if k > 0 and tomatos[i][j][k - 1] == 0:
                tomatos[i][j][k - 1] = 2
                stack.append((i, j, k - 1))
                new += 1
                unriped -= 1
            if i < m - 1 and tomatos[i + 1][j][k] == 0:
                tomatos[i + 1][j][k] = 2
                stack.append((i + 1, j, k))
                new += 1
                unriped -= 1
            if j < n - 1 and tomatos[i][j + 1][k] == 0:
                tomatos[i][j + 1][k] = 2
                stack.append((i, j + 1, k))
                new += 1
                unriped -= 1
            if k < n - 1 and tomatos[i][j][k + 1] == 0:
                tomatos[i][j][k + 1] = 2
                stack.append((i, j, k + 1))
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
