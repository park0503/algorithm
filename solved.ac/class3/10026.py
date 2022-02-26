import sys


def main():
    n = int(sys.stdin.readline())
    img = []
    for _ in range(n):
        img.append(list(sys.stdin.readline().strip()))
    print(img)


main()
