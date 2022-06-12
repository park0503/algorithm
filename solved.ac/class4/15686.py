import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
houses = list()
chickens = list()
cityMaps = dict()
for i in range(n):
    j = 0
    for inp in list(sys.stdin.readline().split()):
        if inp == '1':
            houses.append((i, j))
        elif inp == '2':
            chickens.append((i, j))
        j += 1
chickenCount = len(chickens)
houseCount = len(houses)
for i in range(chickenCount):
    cityMaps[i] = dict()
    for j in range(houseCount):
        cityMaps[i][j] = abs(chickens[i][0] - houses[j][0]) + \
            abs(chickens[i][1] - houses[j][1])
result = 10001
for comb in combinations(range(chickenCount), m):
    minis = [101 for _ in range(houseCount)]
    for num in comb:
        for i in range(houseCount):
            if minis[i] > cityMaps[num][i]:
                minis[i] = cityMaps[num][i]
    suma = sum(minis)
    if result > suma:
        result = suma
print(result)
