import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deque = deque()
for _ in range(n):
    inst = sys.stdin.readline().rstrip()
    if inst[:10] == "push_front":
        num = int(inst[11:])
        deque.appendleft(num)
    elif inst[:9] == "push_back":
        num = int(inst[10:])
        deque.append(num)
    elif inst == "pop_front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.popleft())
    elif inst == "pop_back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.pop())
    elif inst == "size":
        print(len(deque))
    elif inst == "empty":
        if len(deque) == 0:
            print("1")
        else:
            print("0")
    elif inst == "front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[0])
    elif inst == "back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[len(deque) - 1])
