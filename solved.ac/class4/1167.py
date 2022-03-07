from collections import deque
import sys


def main():
    v = int(sys.stdin.readline())
    tree = {}
    result = -1
    for _ in range(v):
        command = list(map(int, sys.stdin.readline().split()[:-1]))
        node = command[0]
        tree[node] = {node: 0}
        for i in range(1, len(command), 2):
            tree[node][command[i]] = command[i + 1]
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i in tree[j]:
                for k in range(1, v + 1):
                    if k in tree[i]:
                        if k not in tree[j] or tree[j][k] > tree[j][i] + tree[i][k]:
                            tree[j][k] = tree[j][i] + tree[i][k]
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if tree[i][j] > result:
                result = tree[i][j]
    print(result)


main()


def main():
    v = int(sys.stdin.readline())
    tree = {}
    result = -1
    for _ in range(v):
        command = list(map(int, sys.stdin.readline().split()[:-1]))
        node = command[0]
        tree[node] = {}
        for i in range(1, len(command), 2):
            tree[node][command[i]] = command[i + 1]
    print(tree)
    for i in range(v):
        for node in tree[i].items():
            stack = deque()
            path = {}
            path.add(i)
            c = node
            while True:
                path.add(c[0])
                for next in tree[c[0]].items():
                    if next[0] not in path and next[0] not in tree[i]:


main()


def main():
    v = int(sys.stdin.readline())
    tree = {}
    result = -1
    for _ in range(v):
        command = list(map(int, sys.stdin.readline().split()[:-1]))
        node = command[0]
        tree[node] = {node: 0}
        for i in range(1, len(command), 2):
            tree[node][command[i]] = command[i + 1]
    c = (1, 0)
    stack = []
    visited = [False for _ in range(v + 1)]
    while True:
        for node in tree[c[0]].items():
            if not visited[node[0]]:
                visited[node[0]] = True
                stack.append(c)
                c = (node[0], c[1] + node[1])
                break

    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if tree[i][j] > result:
                result = tree[i][j]
    print(result)


main()
