import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    t = []
    result = []
    for _ in range(n):
        t.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if i < n - 1:
                vertical = t[i][j] + t[i + 1][j]
                if j < m - 1:
                    result.append(
                        vertical + t[i][j + 1] + t[i + 1][j + 1])  # 정사각형
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
                    if j < m - 1:
                        result.append(vertical + t[i][j + 1])  # 총 모양
                        result.append(vertical + t[i + 2][j + 1])  # 총 모양
                        result.append(vertical + t[i + 1][j + 1])  # 볼록 모양
                if i < n - 3:
                    result.append(vertical + t[i + 3][j])  # 직선
            if j < m - 1:
                horizontal = t[i][j] + t[i][j + 1]
                if i > 0 and i < n - 1:
                    result.append(horizontal + t[i + 1]
                                  [j] + t[i - 1][j + 1])  # 의자 모양
                    result.append(horizontal + t[i - 1]
                                  [j] + t[i + 1][j + 1])  # 의자 모양
                if j < m - 2:
                    horizontal += t[i][j + 2]
                    if i > 0:
                        result.append(horizontal + t[i - 1][j])  # 총 모양
                        result.append(horizontal + t[i - 1][j + 2])  # 총 모양
                        result.append(horizontal + t[i - 1][j + 1])  # 볼록 모양
                    if i < n - 1:
                        result.append(horizontal + t[i + 1][j])  # 총 모양
                        result.append(horizontal + t[i + 1][j + 2])  # 총 모양
                        result.append(horizontal + t[i + 1][j + 1])  # 볼록 모양
                if j < m - 3:
                    result.append(horizontal + t[i][j + 3])  # 직선

    print(max(result))


main()
