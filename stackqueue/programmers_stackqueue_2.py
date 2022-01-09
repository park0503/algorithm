from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    maxElement = max(priorities)
    # any를 쓴다면 max를 안 써도 될 것.
    outCount = 0
    while len(priorities) > 0:
        current = priorities.popleft()
        # deque를 씀으로써 pop(0) 때 들던 시간 복잡도O(n)를 줄일 수 있었다.
        if current < maxElement:
            priorities.append(current)
        else:
            outCount += 1
            if location == 0:
                answer = outCount
                break
            maxElement = max(priorities)
        location = len(priorities) - 1 if location == 0 else location - 1
    return answer
