import sys

n, m = map(int, sys.stdin.readline().split())
t = []
result = []
for _ in range(n):
    t.append(list(map(int, sys.stdin.readline())))


# def straight(vertical, i, j):
#    result = 0
#    for c in range(4):
#        if vertical:
#            result += t[i + c][j]
#        else:
#            result += t[i][j + c]
#    return result
#
# def square(i, j):
#    return t[i][j] + t[i + 1][j] + t[i][j + 1] + t[i + 1][j + 1]
#
# def chair(vertical, right, i, j):
#    result = 0
#    for c in range(3):
#        if vertical:
#            result += t[i + c][j]
#        else:
#            result += t[i][j + c]
#    if vertical and right:
#        result += t[i + ]


for i in range(n):
    for j in range(m):
        if i < n - 1:
            vertical = t[i][j] + t[i + 1][j]
            if j < n - 1:
                result.append(vertical + t[i][j + 1] + t[i + 1][j + 1])  # 정사각형
                if j > 0:
                    result.append(
                        vertical + t[i][j + 1] + t[i + 1][j - 1])  # 의자 모양
                    result.append(
                        vertical + t[i][j - 1] + t[i + 1][j + 1])  # 의자 모양
            if i < n - 2:
                vertical += t[i + 2][j]
                if j > 0:
                    result.append(vertical + t[i][j - 1])  # 총 모양
                    result.append(vertical + t[i + 2][j - 1])  # 총 모양
                    result.append(vertical + t[i + 1][j - 1])  # 볼록 모양
                if j < n - 1:
                    result.append(vertical + t[i][j + 1])  # 총 모양
                    result.append(vertical + t[i + 2][j + 1])  # 총 모양
                    result.append(vertical + t[i + 1][j + 1])  # 볼록 모양
            if i < n - 3:
                result.append(vertical + t[i + 3][j])  # 직선
        if j < n - 1:
            horizontal = t[i][j] + t[i][j + 1]
            if i > 0 and i < n - 1:
                result.append(horizontal + t[i + 1]
                              [j] + t[i - 1][j + 1])  # 의자 모양
                result.append(horizontal + t[i - 1]
                              [j] + t[i + 1][j + 1])  # 의자 모양
            if j < n - 2:
                horizontal += t[i][j + 2]
                if i > 0:
                    result.append(horizontal + t[i - 1][j])  # 총 모양
                    result.append(horizontal + t[i - 1][j + 2])  # 총 모양
                    result.append(horizontal + t[i - 1][j + 1])  # 볼록 모양
                if i < n - 1:
                    result.append(horizontal + t[i + 1][j])  # 총 모양
                    result.append(horizontal + t[i + 1][j + 2])  # 총 모양
                    result.append(horizontal + t[i + 1][j + 1])  # 볼록 모양
            if j < n - 3:
                result.append(horizontal + t[i][j + 3])  # 직선

print(max(result))
