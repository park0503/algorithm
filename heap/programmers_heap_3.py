def solution(operations):
    answer = []
    queue = []
    for op in operations:
        inst = op[0]
        operand = int(op.split()[1])
        if inst == 'I':
            queue.append(operand)
        elif inst == 'D':
            if queue and operand == 1:
                queue.remove(max(queue))
            elif queue and operand == -1:
                queue.remove(min(queue))
    if queue:
        answer.append(max(queue))
        answer.append(min(queue))
    else:
        answer = [0, 0]
    return answer
