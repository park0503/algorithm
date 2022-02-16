import sys

result = [0, 0, 0]
paper = []

n = int(sys.stdin.readline())
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


def checkPaper(rs, cs, l):
    compare = paper[rs][cs]
    for i in range(rs, rs + l):
        for j in range(cs, cs + l):
            if paper[i][j] != compare:
                next = l//3
                checkPaper(rs, cs, next)
                checkPaper(rs, cs + next, next)
                checkPaper(rs, cs + next * 2, next)
                checkPaper(rs + next, cs, next)
                checkPaper(rs + next, cs + next, next)
                checkPaper(rs + next, cs + next * 2, next)
                checkPaper(rs + next * 2, cs, next)
                checkPaper(rs + next * 2, cs + next, next)
                checkPaper(rs + next * 2, cs + next * 2, next)
                return
    result[compare] += 1
    return


checkPaper(0, 0, n)
print(result[-1])
print(result[0])
print(result[1])
