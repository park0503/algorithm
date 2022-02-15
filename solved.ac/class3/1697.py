import math


def main():
    n, k = map(int, input().split())
    if n >= k:
        print(abs(n - k))
        return
    elif k < 2*n:
        print(min([k - n, n*2 - k + 1, n - k//2 +
                   1 + k % 2, n - math.ceil(k/2) + 1 + k % 2]))
        return
    dis = {}
    for i in range(n, k + 1):
        if i == 0:
            dis[i] = 0
            continue
        elif i == 1:
            dis[i] = 1 - n
            continue

        if i >= 2*n:
            dis[i] = min(dis[i//2], dis[math.ceil(i/2)]) + 1 + i % 2
        else:
            dis[i] = min([i - n, n*2 - i + 1, n - i//2 +
                         1 + i % 2, n - math.ceil(i/2) + 1 + i % 2])
    print(dis[k])


main()
