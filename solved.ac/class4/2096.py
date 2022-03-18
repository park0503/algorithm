import sys


def main():
    n = int(sys.stdin.readline())
    dpmax = list(map(int, sys.stdin.readline().split()))
    dpmin = dpmax
    for _ in range(1, n):
        game = list(map(int, sys.stdin.readline().split()))
        dpmax = [max(dpmax[0] + game[0], dpmax[1] + game[0]),
                 max(dpmax[0] + game[1], dpmax[1] +
                     game[1], dpmax[2] + game[1]),
                 max(dpmax[1] + game[2], dpmax[2] + game[2])]
        dpmin = [min(dpmin[0] + game[0], dpmin[1] + game[0]),
                 min(dpmin[0] + game[1], dpmin[1] +
                     game[1], dpmin[2] + game[1]),
                 min(dpmin[1] + game[2], dpmin[2] + game[2])]
    print(max(dpmax), min(dpmin))


main()
