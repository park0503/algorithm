import sys
n = sys.stdin.readline().rstrip()
n = int(n)
result = []
for i in range(n):
    result.append(sys.stdin.readline().rstrip())
result.sort()
result.sort(key=len)
for i in range(len(result)):
    if i != 0 and result[i] == result[i - 1]:
        continue
    else:
        print(result[i])
