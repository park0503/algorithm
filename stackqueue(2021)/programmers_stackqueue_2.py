def solution(progresses, speeds):
    answer = []
    while progresses:
        works = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            works += 1
            if len(progresses) == 0:
                break
        if works != 0:
            answer.append(works)
    return answer
