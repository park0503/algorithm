import sys

def sugar():
    n = int(sys.stdin.readline())
    remaining = n
    vinil = 0
    while remaining % 5 != 0:
        if remaining < 0:
            return -1
        remaining -= 3
        vinil += 1
    vinil += remaining // 5
    return vinil

print(sugar())