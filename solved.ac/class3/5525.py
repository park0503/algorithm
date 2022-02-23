import sys


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    p = list(sys.stdin.readline().strip())
    mode = 0
    l = 0
    r = 0
    for c in p:
        if (mode <= 0) and c == 'I':
            l += 1
            mode = 1
        elif mode > 0 and c == 'O':
            l += 1
            mode = -1
        elif mode != 0:
            l = (l - 1) // 2
            if l >= n:
                r += l - n + 1
            if c == 'I':
                l = 1
                mode = 1
            elif c == 'O':
                l = 0
                mode = 0
    if l > 0:
        l = (l - 1) // 2
        if l >= n:
            r += l - n + 1
    print(r)


main()
