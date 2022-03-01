import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    relation = [[0]*n for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        relation[a - 1][b - 1] = 1
        relation[b - 1][a - 1] = 1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if relation[j][i] and relation[i][k]:
                    if not relation[j][k] or relation[j][k] > relation[j][i] + relation[i][k]:
                        relation[j][k] = relation[j][i] + relation[i][k]
                        relation[k][j] = relation[j][i] + relation[i][k]
    print(relation)
    mini = 5001
    result = -1
    for i in range(n):
        suma = sum(relation[i])
        if suma < mini:
            mini = suma
            result = i
    print(result + 1)


main()
