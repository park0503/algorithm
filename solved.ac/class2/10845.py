import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(n):
    inst = sys.stdin.readline().rstrip()
    if inst[:4] == "push":
        num = int(inst[5:])
        queue.append(num)
    elif inst == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    elif inst == "size":
        print(len(queue))
    elif inst == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif inst == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif inst == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[len(queue) - 1])
