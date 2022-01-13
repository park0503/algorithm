def solution(number, k):
    answer = ''
    i = 0
    while k > 0 and len(number) - 1 > i:
        if int(number[i]) < int(number[i + 1]):
            number = number[:i] + number[i+1:]
            k -= 1
            i = i - 1 if i > 0 else i
        else:
            i += 1
    if k > 0:
        number = number[:len(number) - k]
    answer = number
    return answer
