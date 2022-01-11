def solution(brown, yellow):
    answer = []
    total_count = brown + yellow
    for i in range(1, yellow // 2 + 2):
        if yellow % i == 0:
            a = yellow / i
            if (i + 2) * (a + 2) == total_count:
                answer = [a + 2, i + 2]
                break
    return answer