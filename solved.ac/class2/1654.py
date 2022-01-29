import sys


def main():
    info = sys.stdin.readline()
    k, n = list(map(int, info.split()))
    lans = []
    for i in range(k):
        lans.append(int(sys.stdin.readline()))
    suma = sum(lans)
    maxi = suma // n
    while True:
        tempSum = lans[0] // maxi
        next = lans[0] // (tempSum + 1)
        for i in range(1, len(lans)):
            temp = lans[i] // maxi
            tempSum += temp
            tempNext = lans[i] // ((temp) + 1)
            if tempNext > next:
                next = tempNext
        if tempSum >= n:
            break
        else:
            maxi = next
    print(maxi)


main()
