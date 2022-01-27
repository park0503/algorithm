import sys


def main():
    n = int(sys.stdin.readline())
    alph = sys.stdin.readline()
    M = 1234567891
    answer = 0
    for i in range(n):
        answer += (ord(alph[i]) - 96) * (31 ** i)
    print(answer % M)


main()
