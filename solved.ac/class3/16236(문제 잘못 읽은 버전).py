import sys


def main():
    n = int(sys.stdin.readline())
    sea = []
    counts = [0 for _ in range(7)]
    able = []
    info = {i: [] for i in range(7)}
    si, sj, result = 0, 0, 0
    ssize, exp = 2, 0
    for _ in range(n):
        sea.append(list(map(int, sys.stdin.readline().split())))

    # 물고기 크기 별 마리 수 및 위치, 상어 처음 위치 파악
    for i in range(n):
        for j in range(n):
            current = sea[i][j]
            if current == 9:
                si, sj = i, j
                continue
            if current != 0:
                counts[current] += 1
                info[current].append((i, j))

    able += info[1]

    while True:
        nexti, nextj = -1, -1
        shortest = 50
        index, sindex = 0, 0
        # 가장 가까운 먹을 수 있는 물고기 탐색
        for (k, l) in able:
            temp = abs(si - k) + abs(sj - l)
            if temp < shortest or (temp == shortest and (k < nexti or (k == nexti and l < nextj))):
                shortest = temp
                nexti, nextj = k, l
                sindex = index
            index += 1
        # 못 찾았을 시 break
        if shortest == 50:
            break
        # 찾았을 시 이동 후 섭취
        result += shortest
        si, sj = nexti, nextj
        exp += 1
        # 상어 성장 요건 달성 시 성장
        if exp >= ssize:
            ssize += 1
            if ssize - 1 in info:
                able += info[ssize - 1]
            exp = 0
        # 먹은 물고기 리스트에서 제거
        del able[sindex]

    print(result)


main()
