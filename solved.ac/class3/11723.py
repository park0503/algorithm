import sys


def main():
    m = int(sys.stdin.readline())
    sett = set()
    for _ in range(m):
        c = sys.stdin.readline().split()
        if len(c) < 2:
            if c[0] == "all":
                sett.update({i for i in range(1, 21)})
            elif c[0] == "empty":
                sett.clear()
            continue
        v = int(c[1])
        if c[0] == "add":
            sett.add(v)
        elif c[0] == "remove":
            sett.discard(v)
        elif c[0] == "check":
            if v in sett:
                print(1)
            else:
                print(0)
        elif c[0] == "toggle":
            if v in sett:
                sett.remove(v)
            else:
                sett.add(v)


main()
