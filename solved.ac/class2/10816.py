import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))
data = {a[0]: 1}
for i in range(1, len(a)):
    if a[i] in data:
        data[a[i]] += 1
        continue
    else:
        data[a[i]] = 1
for i in b:
    if i in data:
        print(data[i], end=" ")
    else:
        print("0", end=" ")
