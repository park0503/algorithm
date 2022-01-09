import math


def solution(progresses, speeds):
    answer = []
    remaining = []
    for i in range(len(progresses)):
        remaining.append(math.ceil((100 - progresses[i]) / speeds[i]))
        # 음수의 버림은 양수의 올림과 유사함을 이용해 ceil을 이용하지 않고 푸는 풀이도 존재
    while len(remaining) > 0:
        first = remaining[0]
        count = 0
        remaining = list(map(lambda x: x-first, remaining))
        while len(remaining) > 0 and remaining[0] <= 0:
            remaining.pop(0)
            count += 1
        answer.append(count)
    return answer
