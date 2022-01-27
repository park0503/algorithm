import sys


def main():
    n = int(sys.stdin.readline())
    numbers = {}
    for i in range(n):
        number = int(sys.stdin.readline())
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1
    numbers = sorted(list(numbers.items()), key=lambda x: x[0])
    for number in numbers:
        for i in range(number[1]):
            print(number[0])


main()
