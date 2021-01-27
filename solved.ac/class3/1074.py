import sys

index = 0


def z(size, start_row, start_col):
    global index
    if size == 2:
        for i in range(start_row, start_row + 2):
            for j in range(start_col, start_col + 2):
                if i == r and j == c:
                    print(index)
                    sys.exit()
                else:
                    index += 1
    else:
        size = int(size / 2)
        max_row = start_row + size
        max_col = start_col + size
        if r < max_row and c < max_col:
            z(size, start_row, start_col)
        elif r < max_row and c >= max_col:
            index += size ** 2
            z(size, start_row, max_col)
        elif r >= max_row and c < max_col:
            index += 2 * (size ** 2)
            z(size, max_row, start_col)
        else:
            index += 3 * (size ** 2)
            z(size, max_row, max_col)


n, r, c = map(int, sys.stdin.readline().rstrip().split())
n = 2 ** n
z(n, 0, 0)
