def main():
    n = int(input())
    stairs = []
    maxis = [0 for _ in range(n)]
    for _ in range(n):
        stairs.append(int(input()))
    maxis[0] = stairs[0]
    if n > 1:
        maxis[1] = maxis[0] + stairs[1]
        if n > 2:
            maxis[2] = max(maxis[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n):
        maxis[i] = max(maxis[i - 3] + stairs[i - 1] +
                       stairs[i], maxis[i - 2] + stairs[i])
    print(maxis[n - 1])


main()
