def solution(clothes):
    type = {}
    for cloth in clothes:
        if cloth[1] in type:
            type[cloth[1]] += 1
        else:
            type[cloth[1]] = 1
    answer = 1
    for value in type.values():
        answer *= value + 1
    answer -= 1
    return answer
