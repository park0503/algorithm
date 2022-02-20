import sys

n = int(input())

paper = []
blue = 0
white = 0

for _ in range(n):
    paper.append(list(map(int, list(sys.stdin.readline().split()))))


def dividePaper(rs, cs, l):
    compare = paper[rs][cs]
    global blue, white
    for i in range(rs, rs + l):
        for j in range(cs, cs + l):
            if paper[i][j] != compare:
                next = l // 2
                dividePaper(rs, cs, next)
                dividePaper(rs, cs + next, next)
                dividePaper(rs + next, cs, next)
                dividePaper(rs + next, cs + next, next)
                return
    if compare == 1:
        blue += 1
    else:
        white += 1
    return


dividePaper(0, 0, n)
print(white)
print(blue)
