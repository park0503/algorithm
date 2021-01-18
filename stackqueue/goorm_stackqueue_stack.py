# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from enum import Enum

n = sys.stdin.readline().rstrip()
n = int(n)
stack = []
stack_counter = 0
for _ in range(n):
    num = sys.stdin.readline().rstrip()
    num = int(num)
    if num == 0:
        if stack_counter == 10:
            print("overflow")
            continue
        else:
            num = sys.stdin.readline().rstrip()
            stack.append(num)
            stack_counter += 1
            continue
    elif num == 1:
        if stack_counter == 0:
            print("underflow")
            continue
        else:
            stack.pop()
            stack_counter -= 1
            continue
    else:
        break
for i in stack:
    print(f"{i}", end=" ")
