def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        while k > 0 and len(answer) > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)
