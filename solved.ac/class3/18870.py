import sys


def main():
    n = int(sys.stdin.readline())
    xs = list(map(int, sys.stdin.readline().split()))
    sxs = sorted(set(xs))
    z = {}
    for i in range(len(sxs)):
        z[sxs[i]] = i
    for i in range(len(xs) - 1):
        print(z[xs[i]], end=" ")
    print(z[xs[n-1]])


main()
