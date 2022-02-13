import sys


def main():
    n, m, start = map(int, sys.stdin.readline().split())
    node = {}
    for i in range(n):
        node[i + 1] = [False, False, []]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a not in node[b][2]:
            node[b][2].append(a)
        if b not in node[a][2]:
            node[a][2].append(b)
        node[a][2].sort()
        node[b][2].sort()
    current = start
    dfs = 1
    dfStack = []
    dfsResult = [str(current)]
    bfs = 1
    bfStack = []
    bfsResult = [str(current)]
    node[current][0] = True
    node[current][1] = True
    while dfs < n:
        go = False
        for point in node[current][2]:
            if not node[point][0]:
                node[point][0] = True
                dfsResult.append(str(point))
                dfStack.append(current)
                current = point
                dfs += 1
                go = True
                break
        if not dfStack:
            break
        if not go:
            current = dfStack.pop()
    current = start
    while bfs < n:
        go = False
        for point in node[current][2]:
            if not node[point][1]:
                node[point][1] = True
                bfsResult.append(str(point))
                bfStack.append(point)
                bfs += 1
        if not bfStack:
            break
        current = bfStack.pop(0)
    print(' '.join(dfsResult))
    print(' '.join(bfsResult))


main()
