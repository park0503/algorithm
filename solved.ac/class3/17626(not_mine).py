import sys


def main():
    n = int(sys.stdin.readline())

    if (n ** 0.5) % 1 == 0:
        print(1)
        return

    power = []
    for i in range(1, int(n ** 0.5) + 1):
        power.append(i ** 2)

    for i in power:
        if ((n - i) ** 0.5) % 1 == 0:
            print(2)
            return

    for i in power:
        for j in power:
            if i + j < n and ((n - i - j) ** 0.5) % 1 == 0:
                print(3)
                return
    print(4)
    return


main()
