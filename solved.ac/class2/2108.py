from collections import Counter
import sys
def main():
    n = int(sys.stdin.readline())
    numbers = []
    sum = 0
    for i in range(n):
        num = int(sys.stdin.readline())
        sum += num
        numbers.append(num)
    numbers.sort()
    count_numbers = Counter(numbers)
    most = count_numbers.most_common(n=2)
    print(round(sum/n))
    print(numbers[n//2])
    if n == 1:
        print(numbers[0])
    elif most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
    print(numbers[-1] - numbers[0])

main()