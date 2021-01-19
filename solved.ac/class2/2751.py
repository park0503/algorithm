import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
for i in arr:
    print(i)
