import sys

n = int(input())

video = []

for _ in range(n):
    video.append(list(map(int, list(sys.stdin.readline().strip()))))

result = ""


def divideVideo(rs, cs, l):
    global result
    compare = video[rs][cs]
    for i in range(rs, rs + l):
        for j in range(cs, cs + l):
            if compare != video[i][j]:
                next = l // 2
                result += "("
                divideVideo(rs, cs, next)
                divideVideo(rs, cs + next, next)
                divideVideo(rs + next, cs, next)
                divideVideo(rs + next, cs + next, next)
                result += ")"
                return
    result += str(compare)


divideVideo(0, 0, n)

print(result)
