import sys


def main():
    n = int(sys.stdin.readline())
    img = []
    for _ in range(n):
        img.append(list(sys.stdin.readline().strip()))
    result = [0, 0]
    b = 0
    for mode in range(2):
        check = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if check[i][j] == True or (mode and img[i][j] == "B"):
                    continue
                if img[i][j] == "B":
                    b += 1
                result[mode] += 1
                compare = img[i][j]
                check[i][j] = True
                stack = []
                c = [i, j]
                while True:
                    if mode == 0 and compare != "B":
                        img[c[0]][c[1]] = "Y"
                    if c[0] > 0 and check[c[0] - 1][c[1]] != True and img[c[0] - 1][c[1]] == compare:
                        stack.append([c[0] - 1, c[1]])
                        check[c[0] - 1][c[1]] = True
                    if c[1] > 0 and check[c[0]][c[1] - 1] != True and img[c[0]][c[1] - 1] == compare:
                        stack.append([c[0], c[1] - 1])
                        check[c[0]][c[1] - 1] = True
                    if c[0] < n - 1 and check[c[0] + 1][c[1]] != True and img[c[0] + 1][c[1]] == compare:
                        stack.append([c[0] + 1, c[1]])
                        check[c[0] + 1][c[1]] = True
                    if c[1] < n - 1 and check[c[0]][c[1] + 1] != True and img[c[0]][c[1] + 1] == compare:
                        stack.append([c[0], c[1] + 1])
                        check[c[0]][c[1] + 1] = True
                    if stack:
                        c = stack.pop()
                    else:
                        break
    print(str(result[0]) + " " + str(result[1] + b))


main()
