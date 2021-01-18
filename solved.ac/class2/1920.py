import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()
for i in b:
    start = 0
    end = n
    find = 0
    while end > start:
        mid = int((start + end) / 2)
        if i < a[mid]:
            end = mid
            continue
        elif i > a[mid]:
            start = mid + 1
            continue
        else:
            find = 1
            break
    print(find)
