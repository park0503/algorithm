n = int(input())
stars = [[" " for _ in range(n + n)] for i in range(n)]


def chopStar(top, bottom, center):
    height = bottom - top
    if height > 3:
        temp = height // 2
        chopStar(top, top + temp, center)
        chopStar(top + temp, bottom, center - temp)
        chopStar(top + temp, bottom, center + temp)
        return
    stars[top][center] = "*"
    stars[top + 1][center - 1] = "*"
    stars[top + 1][center + 1] = "*"
    for i in range(3):
        stars[top + 2][center + i] = "*"
        stars[top + 2][center - i] = "*"
    return


chopStar(0, n, n - 1)

for row in stars:
    print(''.join(row))
