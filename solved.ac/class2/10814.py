import sys

n = int(sys.stdin.readline().rstrip())
users = []
for i in range(n):
    data = {}
    data['age'], data['name'] = sys.stdin.readline().rstrip().split()
    data['age'] = int(data['age'])
    users.append(data)
users = sorted(users, key=lambda x: x['age'])
for i in users:
    print(i['age'], end=" ")
    print(i['name'])
