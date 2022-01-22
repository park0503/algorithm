def main():
    while True:
        triangle = input()
        triangle = sorted(list(map(int, triangle.split())))
        if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
            break
        elif triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
            print("right")
        else:
            print("wrong")


main()
