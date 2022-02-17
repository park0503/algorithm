import sys


def main():
    n, m = map(int, input().split())
    maze = []
    stack = []
    current = (0, 0, 1)
    end = n + m - 2
    for _ in range(n):
        maze.append(list(map(int, list(sys.stdin.readline().strip()))))
    maze[0][0] = 2
    while current[0] + current[1] < end:
        if current[0] > 0 and maze[current[0] - 1][current[1]] == 1:
            stack.append((current[0] - 1, current[1], current[2] + 1))
            maze[current[0] - 1][current[1]] = 2
        if current[1] > 0 and maze[current[0]][current[1] - 1] == 1:
            stack.append((current[0], current[1] - 1, current[2] + 1))
            maze[current[0]][current[1] - 1] = 2
        if current[0] < n - 1 and maze[current[0] + 1][current[1]] == 1:
            stack.append((current[0] + 1, current[1], current[2] + 1))
            maze[current[0] + 1][current[1]] = 2
        if current[1] < m - 1 and maze[current[0]][current[1] + 1] == 1:
            stack.append((current[0], current[1] + 1, current[2] + 1))
            maze[current[0]][current[1] + 1] = 2
        current = stack.pop(0)
    print(current[2])


main()
