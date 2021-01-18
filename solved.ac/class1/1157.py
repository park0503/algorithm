import sys

s = sys.stdin.readline().rstrip()
data = {}
for i in s:
    if ord(i) >= 97:
        temp = ord(i) - 32
        temp = chr(temp)
    else:
        temp = i
    if temp in data:
        data[temp] += 1
    else:
        data[temp] = 1
data = sorted(data.items(), key=lambda x: x[1], reverse=True)
if len(data) > 1 and data[0][1] == data[1][1]:
    print("?")
else:
    print(data[0][0])
