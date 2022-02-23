import sys


def main():
    result = []
    n = int(sys.stdin.readline())
    zido = []
    for _ in range(n):
        zido.append(list(map(int, list(sys.stdin.readline().strip()))))
    for i in range(n):
        for j in range(n):
            if zido[i][j] == 1:
                count = 1
                c = (i, j)
                stack = []
                while True:
                    zido[c[0]][c[1]] = 2
                    if c[0] > 0 and zido[c[0] - 1][c[1]] == 1:
                        stack.append(c)
                        c = (c[0] - 1, c[1])
                        count += 1
                    elif c[1] > 0 and zido[c[0]][c[1] - 1] == 1:
                        stack.append(c)
                        c = (c[0], c[1] - 1)
                        count += 1
                    elif c[0] < n - 1 and zido[c[0] + 1][c[1]] == 1:
                        stack.append(c)
                        c = (c[0] + 1, c[1])
                        count += 1
                    elif c[1] < n - 1 and zido[c[0]][c[1] + 1] == 1:
                        stack.append(c)
                        c = (c[0], c[1] + 1)
                        count += 1
                    elif stack:
                        c = stack.pop()
                    else:
                        break
                result.append(count)
    result.sort()
    print(len(result))
    for num in result:
        print(num)


main()
