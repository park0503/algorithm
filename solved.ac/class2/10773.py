import sys


def main():
    k = int(sys.stdin.readline())
    numbers = []
    for i in range(k):
        current = int(sys.stdin.readline())
        if current == 0:
            numbers.pop()
        else:
            numbers.append(current)
    print(sum(numbers))


main()
