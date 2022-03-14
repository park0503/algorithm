import sys
from collections import deque


def main():
    sikk = list(sys.stdin.readline().strip())
    result = ""
    ops = deque()
    rank = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2}
    for el in sikk:
        if el >= 'A' and el <= 'Z':
            result += el
        else:
            if el == ")":
                while ops[0] != "(":
                    result += ops.popleft()
                ops.popleft()
            else:
                while ops and ops[0] != "(" and rank[ops[0]] >= rank[el]:
                    result += ops.popleft()
                ops.appendleft(el)
    while ops:
        result += ops.popleft()
    print(result)


main()
