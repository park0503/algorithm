import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    inst = sys.stdin.readline().rstrip()
    if inst[:4] == "push":
        num = int(inst[5:])
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
