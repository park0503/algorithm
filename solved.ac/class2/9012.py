import sys

n = int(sys.stdin.readline().rstrip())
pss = []
for i in range(n):
    ps = sys.stdin.readline().rstrip()
    pss.append(ps)
for i in pss:
    open_p = 0
    correctness = 1
    for j in i:
        if j == '(':
            open_p += 1
        else:
            if open_p == 0:
                correctness = 0
                break
            else:
                open_p -= 1
    if correctness == 1 and open_p == 0:
        print("YES")
    else:
        print("NO")
