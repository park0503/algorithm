import sys


def main():
    n = int(sys.stdin.readline())
    graph = []
    check = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and check[i][j] == False:
                c = j
                stack = []
                while True:
                    graph[i][c] = True
                    for k in range(n):
                        if graph[c][k] == 1 and graph[i][k] != 1:
                            stack.append(k)
                            graph[i][k] = 1
                    if stack:
                        c = stack.pop()
                    else:
                        break
    for i in range(n):
        for j in range(n):
            print(int(graph[i][j]), end=" ")
        print("")


main()
