import sys

def main():
    n = int(sys.stdin.readline())
    numbers = []
    for _ in range(n):
        numbers.append(int(sys.stdin.readline()))
    habs = [0 for _ in range(12)]
    habs[0] = 1
    habs[1] = 1
    habs[2] = 2
    count = 3
    for number in numbers:
        if number < count:
            print(habs[number])
            continue
        for i in range(count, number + 1):
            habs[i] = habs[i - 3] + habs[i - 2] + habs[i - 1]
        count = number + 1
        print(habs[number])

main()