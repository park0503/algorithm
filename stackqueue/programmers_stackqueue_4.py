def solution(priorities, location):
    answer = 0
    time = 0
    while answer == 0:
        check = 0
        for i in priorities:
            if i > priorities[0]:
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1
                temp = priorities.pop(0)
                priorities.append(temp)
                check = 1
                break
        if check == 0:
            priorities.pop(0)
            time += 1
            if location == 0:
                answer = time
                break
            else:
                location -= 1
    return answer
