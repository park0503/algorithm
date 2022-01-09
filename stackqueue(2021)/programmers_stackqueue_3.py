from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing = deque()
    time = deque()
    after = deque()
    total = 0
    while len(truck_weights) > 0 or len(crossing) > 0:
        if time and (time[0] + bridge_length) == answer:
            time.popleft()
            total -= crossing[0]
            after.append(crossing.popleft())
        if truck_weights and total+truck_weights[0] <= weight:
            total += truck_weights[0]
            crossing.append(truck_weights.pop(0))
            time.append(answer)
        answer += 1
    return answer
