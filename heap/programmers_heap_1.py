import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + 2 * b
        heapq.heappush(scoville, c)
        answer += 1
    return answer
