import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
square = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    square.append(line)
minimum = 64
for i in range(0, n - 7):
    for j in range(0, m - 7):
        if square[i][j] == 'W':
            color = 0
        else:
            color = 1
        temp = 0
        for k in range(i, i + 8):
            for w in range(j, j + 8):
                row = k % 2
                col = w % 2
                if color == 0:
                    if row == col:
                        if square[k][w] != 'W':
                            temp += 1
                    else:
                        if square[k][w] != 'B':
                            temp += 1
                else:
                    if row == col:
                        if square[k][w] != 'B':
                            temp += 1
                    else:
                        if square[k][w] != 'W':
                            temp += 1
        if temp > 32:
            temp = 64 - temp
        if temp < minimum:
            minimum = temp
        print(minimum)
print(minimum)
