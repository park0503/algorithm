def solution(prices):
    answer = []
    for j in range(0, len(prices)):
        time = 0
        for i in range(j+1, len(prices)):
            time += 1
            if prices[j] > prices[i]:
                break
        answer.append(time)
    return answer
