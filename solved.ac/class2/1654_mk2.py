import sys


def main():
    info = sys.stdin.readline()
    k, n = list(map(int, info.split()))
    lans = []
    for i in range(k):
        lans.append(int(sys.stdin.readline()))
    suma = sum(lans)
    right = suma // n
    left = 0
    result = 0
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for lan in lans:
            temp += lan // mid
        if temp < n:
            right = mid - 1
        else:
            left = mid + 1
            result = mid
    print(result)

main()
