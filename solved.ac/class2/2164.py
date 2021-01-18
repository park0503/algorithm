import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
card = deque()
for i in range(1, n + 1):
    card.append(i)
while len(card) != 1:
    card.popleft()
    temp = card.popleft()
    card.append(temp)
print(card[0])
