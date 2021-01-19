import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    inst = sys.stdin.readline().split()[0]
    if inst == "push":
        num = int(sys.stdin.readline().split()[1])
        stack.append(num)
    elif inst == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif inst == "size":
        print(len(stack))
    elif inst == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif inst == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[len(stack) - 1])
