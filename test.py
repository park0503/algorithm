def main():
    start, end = map(int, input().split())
    numbers = {}
    for i in range(0, end + 1):
        if i not in numbers:
            if i > 1:
                numbers[i] = True
            else:
                numbers[i] = False
        if numbers[i]:
            p = 2
            while p * i <= end:
                numbers[p * i] = False
                p += 1
    numbers = sorted(list(numbers.items()), key=lambda x: x[0])
    for i in range(start, end + 1):
        if numbers[i][1]:
            print(numbers[i][0])


main()
