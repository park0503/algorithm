import sys
def main():
    n = int(sys.stdin.readline())
    p = 1
    temp = 1
    while temp < n:
        temp += p * 6
        p += 1
    print(p)

main()