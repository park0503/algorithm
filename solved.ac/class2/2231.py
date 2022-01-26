import sys

def problem():
    n = int(sys.stdin.readline())
    if n < 10:
        if n % 2 == 0:
            return n // 2
        else:
            return 0
    strn = str(n)
    back = strn[1:]
    check = n - len(back) * 9 - int(strn[0])
    while check <= n:
        temp = check
        for num in str(check):
            temp += int(num)
        if temp == n:
            return check
        check += 1
    return 0

print(problem())