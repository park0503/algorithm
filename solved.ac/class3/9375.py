import sys


t = int(sys.stdin.readline())


for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    result = 1
    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]
    clothes = list(clothes.items())
    for cloth in clothes:
        result *= len(cloth[1]) + 1
    print(result - 1)
