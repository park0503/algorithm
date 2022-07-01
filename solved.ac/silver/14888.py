import sys
from itertools import permutations

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
opinput = list(map(int, sys.stdin.readline().split()))
table = {0: '+', 1: '-', 2: '*', 3: '/'}
answer = set()
operations = []
for i, count in enumerate(opinput):
    for _ in range(count):
        operations.append(table[i])
for ops in set(permutations(operations, n - 1)):
    temp = numbers[0]
    for i in range(1, n):
        if ops[i - 1] == '+':
            temp += numbers[i]
        elif ops[i - 1] == '-':
            temp -= numbers[i]
        elif ops[i - 1] == '*':
            temp *= numbers[i]
        elif ops[i - 1] == '/':
            if temp < 0:
                temp = -1 * (-1 * temp // numbers[i])
            else:
                temp //= numbers[i]
    answer.add(temp)
print(max(answer))
print(min(answer))
