from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(people.sort())
    while people:
        current = 0
        while people and current + people[-1] <= limit:
            current += people.pop()
        while people and current + people[0] <= limit:
            current += people.popleft()
        answer += 1
    return answer


solution([70, 50, 80, 50], 100)
