def main():
    n = int(input())
    count = 0
    num = "665"
    while count != n:
        num = int(num) + 1
        if "666" in str(num):
            count += 1
    print(num)


main()
