# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
maze = [0 for _ in range(4)]
check = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
path = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(4):
    maze[i] = list(map(int, input().split()))
stack = []
stack_counter = 0
data = {'x': 0, 'y': 0}
stack.append(data)
for i in range(16):
    x = stack[stack_counter]['x']
    y = stack[stack_counter]['y']
    if y + 1 < 4 and maze[x][y + 1] == 1 and check[x][y + 1] == 0 and path[x][y + 1] == 0:
        y += 1
    elif x + 1 < 4 and maze[x + 1][y] == 1 and check[x + 1][y] == 0 and path[x + 1][y] == 0:
        x += 1
    elif y - 1 >= 0 and maze[x][y - 1] == 1 and check[x][y - 1] == 0 and path[x][y - 1] == 0:
        y -= 1
    elif x - 1 >= 0 and maze[x - 1][y] == 1 and check[x - 1][y] == 0 and path[x - 1][y] == 0:
        x -= 1
    else:
        check[x][y] = 1
        stack.pop()
        stack_counter -= 1
        continue
    path[x][y] = 1
    data = {'x': x, 'y': y}
    stack.append(data)
    stack_counter += 1
    if x == 3 and y == 3:
        break
for i in range(4):
    for j in range(4):
        print(f" {path[i][j]} ", end="")
    print("")
