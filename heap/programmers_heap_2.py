import heapq
from collections import deque


def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[0])
    job_count = len(jobs)
    jobs = deque(jobs)
    current_time = 0
    available = []
    while jobs or available:
        while jobs:
            job = jobs[0]
            if current_time < job[0]:
                if not available:
                    current_time = job[0]
                break
            heapq.heappush(available, (job[1], job[0]))
            jobs.popleft()
        if available:
            to_do = heapq.heappop(available)
            current_time += to_do[0]
            answer += current_time - to_do[1]
    answer /= job_count
    return int(answer)
