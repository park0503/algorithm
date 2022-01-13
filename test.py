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
    print(states)
    while len(cover) < count:
        ongoing = []
        check = False
        for state in states:
            if state[1] in ongoing:
                check = True
            else:
                ongoing.append(state[1])
            if check and prev != state[0]:
                break
            prev = state[0]
        cover += ongoing
        answer += 1
        nex = []
        for state in states:
            print(state)
            if state[1] not in cover:
                nex.append(state[1])
        states = nex
    return answer


solution([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [
         8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]])
