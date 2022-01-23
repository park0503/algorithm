def main():
    start, end = map(int, input().split())
    numbers = {}
    for i in range(1, end + 1):
        if i not in numbers:
            numbers[i] = True
        if i > 1 and numbers[i]:
            p = 2
            while p * i <= end:
                numbers[p * i] = False
                p += 1
    numbers = sorted(list(numbers.items()), key=lambda x: x[0])
    for i in range(start, end):
        if numbers[i][1]:
            print(numbers[i][0])


main()
