import sys


def remoteCon():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    numbers = [True for i in range(10)]
    if m != 0:
        brokens = sys.stdin.readline().split()
        for broken in brokens:
            numbers[int(broken)] = False
    if n == 100:
        print(0)
        return 0
    direct = abs(n - 100)

    bottom = 1000000
    top = 1000000
    for channel in range(n, -1, -1):
        find = True
        for i in str(channel):
            if not numbers[int(i)]:
                find = False
                break
        if find:
            bottom = channel
            break
    for channel in range(n + 1, 1000000):
        find = True
        for i in str(channel):
            if not numbers[int(i)]:
                find = False
                break
        if find:
            top = channel
            break
    winner = top if abs(top - n) < abs(bottom - n) else bottom
    output = len(str(winner)) + abs(winner - n)
    result = output if output < direct else direct
    print(result)


remoteCon()
