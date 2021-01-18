from collections import deque


def solution(prices):
    answer = [0] * len(prices)
    stock = deque()
    how_much = deque()
    index = deque()
    time = 0
    while prices:
        time += 1
        while stock and stock[0] > prices[0]:
            stock.popleft()
            answer[index.popleft()] = time - how_much.popleft()
        stock.appendleft(prices.pop(0))
        how_much.appendleft(time)
        index.appendleft(time - 1)
    while stock:
        stock.popleft()
        answer[index.popleft()] = time - how_much.popleft()
    return answer
