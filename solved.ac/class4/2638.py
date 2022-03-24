import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    result = 0
    paper = []
    for _ in range(n):
        paper.append(list(map(int, sys.stdin.readline().split())))

    # 외부 공기만 -1로 치환하기 위한 bfs
    stack = []
    stack.append((0, 0))
    cheeze = set()
    paper[0][0] = -1
    while stack:
        i, j = stack.pop()
        if i > 0 and paper[i - 1][j] == 0:
            paper[i - 1][j] = -1
            stack.append((i - 1, j))
        if j > 0 and paper[i][j - 1] == 0:
            paper[i][j - 1] = -1
            stack.append((i, j - 1))
        if i < n - 1 and paper[i + 1][j] == 0:
            paper[i + 1][j] = -1
            stack.append((i + 1, j))
        if j < m - 1 and paper[i][j + 1] == 0:
            paper[i][j + 1] = -1
            stack.append((i, j + 1))

    # 남아있는 치즈의 집합 cheeze 채우기
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1:
                cheeze.add((i, j))

    # 본 작업
    while cheeze:
        result += 1
        expired = []
        # 남아있는 치즈들에 대해서 외부 공기와 접촉 면적이 2개 이상이면 expired에 추가
        for i, j in cheeze:
            if paper[i][j] == 1:
                count = 0
                if i > 0 and paper[i - 1][j] == -1:
                    count += 1
                if j > 0 and paper[i][j - 1] == -1:
                    count += 1
                if i < n - 1 and paper[i + 1][j] == -1:
                    count += 1
                if j < m - 1 and paper[i][j + 1] == -1:
                    count += 1
                if count > 1:
                    expired.append((i, j))

        # 탐색이 끝난 사라져야할 치즈들을 제거 & 외부공기와 맞닿은 내부공기들 외부공기로 치환
        for oi, oj in expired:
            stack = []
            stack.append((oi, oj))
            paper[oi][oj] = -1
            cheeze.remove((oi, oj))
            while stack:
                i, j = stack.pop()
                if i > 0 and paper[i - 1][j] == 0:
                    paper[i - 1][j] = -1
                    stack.append((i - 1, j))
                if j > 0 and paper[i][j - 1] == 0:
                    paper[i][j - 1] = -1
                    stack.append((i, j - 1))
                if i < n - 1 and paper[i + 1][j] == 0:
                    paper[i + 1][j] = -1
                    stack.append((i + 1, j))
                if j < m - 1 and paper[i][j + 1] == 0:
                    paper[i][j + 1] = -1
                    stack.append((i, j + 1))
    print(result)


main()
