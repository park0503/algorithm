import sys

inp = sys.stdin.readline().strip()
trigger = list(sys.stdin.readline().strip())
length = len(trigger)
result = list()

for el in inp:
    result.append(el)
    if el == trigger[-1] and result[-1 * length:] == trigger:
        del result[-1 * length:]

if result:
    print(''.join(result))
else:
    print("FRULA")
