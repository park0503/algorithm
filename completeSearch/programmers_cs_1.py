def solution(answers):
    sik = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    count = [0 for i in range(3)]
    answer = []
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == sik[j][i % len(sik[j])]:
                count[j] += 1
    maxScore = max(count)
    for i in range(3):
        if count[i] == maxScore:
            answer.append(i + 1)
    return answer