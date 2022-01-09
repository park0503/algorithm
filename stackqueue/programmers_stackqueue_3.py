from collections import deque


def solution(bridge_length, weight, truck_weights):
    current_weight = 0
    truck_weights = deque(truck_weights)
    moving_trucks = deque()
    answer = 0
    while len(truck_weights) > 0 or len(moving_trucks) > 0:
        answer += 1
        if len(moving_trucks) > 0 and answer - moving_trucks[0][0] >= bridge_length:
            out = moving_trucks.popleft()
            current_weight -= out[1]
        if len(truck_weights) > 0 and current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            truck = (answer, truck_weights.popleft())
            moving_trucks.append(truck)
    return answer
