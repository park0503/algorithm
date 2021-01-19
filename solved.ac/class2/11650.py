import sys

t = int(sys.stdin.readline().rstrip())
point = []
for _ in range(t):
    data = {}
    data['x'], data['y'] = map(int, sys.stdin.readline().rstrip().split())
    point.append(data)
point = sorted(point, key=lambda x: x['y'])
point = sorted(point, key=lambda x: x['x'])
for i in point:
    print(i['x'], i['y'])
