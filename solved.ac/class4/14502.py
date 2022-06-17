from copy import deepcopy
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
research = []
for _ in range(n):
    research.append(list(map(int, sys.stdin.readline().split())))
blank = []
for i in range(n):
    for j in range(m):
        if research[i][j] == 0:
            blank.append((i, j))
maxi = -1
for case in combinations(blank, 3):
    tempResearch = deepcopy(research)
    for i in range(3):
        tempResearch[case[i][0]][case[i][1]] = 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and tempResearch[i][j] == 2:
                stack = []
                stack.append((i, j))
                visited[i][j] = True
                while stack:
                    ci, cj = stack.pop()
                    if ci > 0 and tempResearch[ci - 1][cj] == 0:
                        tempResearch[ci - 1][cj] = 2
                        visited[ci - 1][cj] = True
                        stack.append((ci - 1, cj))
                    if cj > 0 and tempResearch[ci][cj - 1] == 0:
                        tempResearch[ci][cj - 1] = 2
                        visited[ci][cj - 1] = True
                        stack.append((ci, cj - 1))
                    if ci + 1 < n and tempResearch[ci + 1][cj] == 0:
                        tempResearch[ci + 1][cj] = 2
                        visited[ci + 1][cj] = True
                        stack.append((ci + 1, cj))
                    if cj + 1 < m and tempResearch[ci][cj + 1] == 0:
                        tempResearch[ci][cj + 1] = 2
                        visited[ci][cj + 1] = True
                        stack.append((ci, cj + 1))
    count = 0
    for i in range(n):
        for j in range(m):
            if tempResearch[i][j] == 0:
                count += 1
    if count > maxi:
        maxi = count
print(maxi)
