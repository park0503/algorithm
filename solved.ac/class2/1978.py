import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
for i in a:
    if i == 1:
        continue
    elif i == 2:
        count += 1
        continue
    find = 1
    for j in range(2, round(i / 2) + 1):
        if i % j == 0:
            find = 0
            break
    count += find
print(count)
