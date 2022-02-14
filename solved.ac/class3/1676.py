import sys


def main():
    n = int(sys.stdin.readline())
    pacs = [[0, 0] for _ in range(n+1)]
    for i in range(2, n + 1):
        temp = i
        while temp > 1:
            if temp % 2 == 0:
                pacs[i][0] += 1
                temp //= 2
            elif temp % 5 == 0:
                pacs[i][1] += 1
                temp //= 5
            else:
                break
        pacs[i][0] += pacs[i - 1][0]
        pacs[i][1] += pacs[i - 1][1]
    print(min(pacs[n]))


main()
