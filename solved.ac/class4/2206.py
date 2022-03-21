import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = []
    visited = [[[1000001 for _ in range(m)]
                for _ in range(n)]for _ in range(2)]
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip())))
    stack = deque()
    stack.append((0, 0, 1, 0))
    visited[0][0][0] = 1
    while stack:
        i, j, dist, hammer = stack.popleft()
        dist += 1
        if i > 0 and visited[hammer][i - 1][j] > dist:
            if graph[i - 1][j] == 0:
                stack.append((i - 1, j, dist, hammer))
                visited[hammer][i - 1][j] = dist
            elif hammer == 0:
                stack.append((i - 1, j, dist, 1))
                visited[1][i - 1][j] = dist
        if j > 0 and visited[hammer][i][j - 1] > dist:
            if graph[i][j - 1] == 0:
                stack.append((i, j - 1, dist, hammer))
                visited[hammer][i][j - 1] = dist
            elif hammer == 0:
                stack.append((i, j - 1, dist, 1))
                visited[1][i][j - 1] = dist
        if i < n - 1 and visited[hammer][i + 1][j] > dist:
            if graph[i + 1][j] == 0:
                stack.append((i + 1, j, dist, hammer))
                visited[hammer][i + 1][j] = dist
            elif hammer == 0:
                stack.append((i + 1, j, dist, 1))
                visited[1][i + 1][j] = dist
        if j < m - 1 and visited[hammer][i][j + 1] > dist:
            if graph[i][j + 1] == 0:
                stack.append((i, j + 1, dist, hammer))
                visited[hammer][i][j + 1] = dist
            elif hammer == 0:
                stack.append((i, j + 1, dist, 1))
                visited[1][i][j + 1] = dist
    result = min(visited[0][n - 1][m - 1], visited[1][n - 1][m - 1])
    if result > 1000000:
        print(-1)
    else:
        print(result)


main()
