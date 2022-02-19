import sys


def main():
    computers = {}
    n = int(input())
    visited = [False for _ in range(n)]
    count = 0
    stack = [1]
    current = 1
    m = int(input())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a in computers:
            computers[a].append(b)
        else:
            computers[a] = [b]
        if b in computers:
            computers[b].append(a)
        else:
            computers[b] = [a]
    visited[0] = True
    while True:
        throw = False
        if current in computers:
            for next in computers[current]:
                if not visited[next - 1]:
                    visited[next - 1] = True
                    stack.append(current)
                    current = next
                    count += 1
                    throw = True
                    break
        if throw:
            continue
        elif stack:
            current = stack.pop()
        else:
            break
    print(count)


main()
