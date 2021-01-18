def solution(prices):
    answer = []
    while prices:
        time = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            time += 1
            if prices[0] > prices[i]:
                break
        answer.append(time)
        prices.pop(0)
    return answer
