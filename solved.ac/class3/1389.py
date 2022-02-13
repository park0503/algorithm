import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    relation = [[-1]*n for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        relation[a - 1][b - 1] = 1
        relation[b - 1][a - 1] = 1
    for i in range(n):
        for j in range(n):
            if relation[i][j] != -1:
                for k in range(n):
                    if relation[j][k] != -1:
                        temp = relation[i][j] + relation[j][k]
                        if relation[i][k] == -1 or relation[i][k] > temp:
                            relation[i][k] = temp
                            relation[k][i] = temp
    mini = 5001
    result = -1
    for i in range(n):
        suma = sum(relation[i])
        if suma < mini:
            mini = suma
            result = i
    print(result + 1)


main()
