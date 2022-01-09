import math


def solution(n):
    answer = 0
    li = [True for num in range(n+1)]
    for num in range(2, int(math.sqrt(n)) + 1):
        if li[num]:
            p = 2
            while num * p < n + 1:
                li[num * p] = False
                p += 1
    for num in range(2, n+1):
        if li[num]:
            answer += 1
    return answer
