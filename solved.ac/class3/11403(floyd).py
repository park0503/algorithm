import sys


def main():
    n = int(sys.stdin.readline())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if not graph[j][k] and graph[j][i] and graph[i][k]:
                    graph[j][k] = 1

    for i in range(n):
        for j in range(n):
            print(int(graph[i][j]), end=" ")
        print("")


main()
