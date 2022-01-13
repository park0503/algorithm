def solution(routes):
    answer = 0
    count = len(routes)
    cover = []
    states = []
    for i in range(count):
        if i in cover:
            continue
        states.append([routes[i][0], i])
        states.append([routes[i][1], i])
    states.sort(key=lambda x: x[0])
    while states:
        ongoing = []
        check = False
        for state in states:
            if check and prev != state[0]:
                break
            if state[1] in ongoing:
                check = True
            else:
                ongoing.append(state[1])
            prev = state[0]
        answer += 1
        nex = []
        for state in states:
            if state[1] not in ongoing:
                nex.append(state)
        states = nex
    return answer
