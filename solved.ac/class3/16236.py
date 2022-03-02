import sys
from collections import deque


def main():
    n = int(sys.stdin.readline())
    sea = []
    si, sj, result = 0, 0, 0
    ssize, exp = 2, 0
    for _ in range(n):
        sea.append(list(map(int, sys.stdin.readline().split())))

    # 물고기 크기 별 마리 수 및 위치, 상어 처음 위치 파악
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sea[i][j] = 0
                si, sj = i, j
                break

    while True:
        tempi, tempj = si, sj
        stack = deque()
        distance, checkd = 0, 0
        check = [[False for _ in range(n)] for _ in range(n)]
        check[tempi][tempj] = True
        end = False
        candidate = []
        while True:
            if distance > checkd:
                if candidate:
                    mini, minj = 21, 21
                    result += distance
                    for (i, j) in candidate:
                        if i < mini or (i == mini and j < minj):
                            mini, minj = i, j
                    si, sj = mini, minj
                    sea[si][sj] = 0
                    exp += 1
                    if exp >= ssize:
                        ssize += 1
                        exp = 0
                    break
                checkd += 1
            distance += 1
            if tempi > 0 and not check[tempi - 1][tempj] and sea[tempi - 1][tempj] <= ssize:
                if sea[tempi - 1][tempj] and sea[tempi - 1][tempj] < ssize:
                    candidate.append((tempi - 1, tempj))
                check[tempi - 1][tempj] = True
                stack.append((tempi - 1, tempj, distance))
            if tempj > 0 and not check[tempi][tempj - 1] and sea[tempi][tempj - 1] <= ssize:
                if sea[tempi][tempj - 1] and sea[tempi][tempj - 1] < ssize:
                    candidate.append((tempi, tempj - 1))
                check[tempi][tempj - 1] = True
                stack.append((tempi, tempj - 1, distance))
            if tempi < n - 1 and not check[tempi + 1][tempj] and sea[tempi + 1][tempj] <= ssize:
                if sea[tempi + 1][tempj] and sea[tempi + 1][tempj] < ssize:
                    candidate.append((tempi + 1, tempj))
                check[tempi + 1][tempj] = True
                stack.append((tempi + 1, tempj, distance))
            if tempj < n - 1 and not check[tempi][tempj + 1] and sea[tempi][tempj + 1] <= ssize:
                if sea[tempi][tempj + 1] and sea[tempi][tempj + 1] < ssize:
                    candidate.append((tempi, tempj + 1))
                check[tempi][tempj + 1] = True
                stack.append((tempi, tempj + 1, distance))
            if stack:
                next = stack.popleft()
                tempi, tempj, distance = next[0], next[1], next[2]
            elif candidate:
                continue
            else:
                end = True
                break
        if end:
            break
    print(result)


main()
