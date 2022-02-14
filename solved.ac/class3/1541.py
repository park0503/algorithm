import sys


def main():
    sik = sys.stdin.readline()
    stack = []
    check = 0
    for i in range(len(sik)):
        if sik[i] == '+' or sik[i] == '-' or sik[i] == '\n':
            stack.append(sik[check:i])
            stack.append(sik[i])
            check = i + 1
    stack.pop()

    result = 0
    mode = True
    for node in stack:
        if node == '-':
            mode = False
        elif node != '+':
            if mode:
                result += int(node)
            else:
                result -= int(node)
    print(result)


main()
