import sys

v = int(sys.stdin.readline())
tree = {}
result = 0
rotate = 1
for _ in range(v):
    command = list(map(int, sys.stdin.readline().split()[:-1]))
    node = command[0]
    tree[node] = {}
    for i in range(1, len(command), 2):
        tree[node][command[i]] = command[i + 1]

visited = [False for _ in range(v + 1)]
visited[1] = True


def dfs(n, dist):
    global result, rotate
    if dist > result:
        result = dist
        rotate = n
    for node in tree[n].items():
        if visited[node[0]]:
            continue
        visited[node[0]] = True
        dfs(node[0], dist + node[1])


dfs(rotate, 0)
visited = [False for _ in range(v + 1)]
visited[rotate] = True
dfs(rotate, 0)
print(result)
