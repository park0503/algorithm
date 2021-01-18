import sys

while True:
    data = sys.stdin.readline().rstrip()
    if data == '0':
        break
    start = 0
    end = len(data) - 1
    is_palindrome = 1
    while end > start:
        if data[start] != data[end]:
            is_palindrome = 0
            break
        start += 1
        end -= 1
    if is_palindrome == 1:
        print("yes")
    else:
        print("no")
