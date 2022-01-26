import sys
def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        apt = [[temp + 1 for temp in range(n)]]
        for j in range(1,k+1):
            floor = []
            for l in range(n):
                temp = 0
                for hek in range(l + 1):
                    temp += apt[j - 1][hek]
                floor.append(temp)
            apt.append(floor)
        print(apt[k][n-1])

main()