import sys


def main():
    n = int(sys.stdin.readline())
    result = 0
    while n > 4:
        result += n//5
        n //= 5
    print(result)


main()
