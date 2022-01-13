def solution(n, costs):
    answer = 0
    progress = [0]
    info = {}
    for cost in costs:
        if cost[0] in info:
            info[cost[0]].append((cost[2], cost[1]))
        else:
            info[cost[0]] = [(cost[2], cost[1])]
        if cost[1] in info:
            info[cost[1]].append((cost[2], cost[0]))
        else:
            info[cost[1]] = [(cost[2], cost[0])]
    info = list(info.items())
    info.sort(key=lambda x: x[0])
    while len(progress) < n:
        mini = (999999999,)
        for complete in progress:
            for dis in info[complete][1]:
                if dis[1] not in progress and mini[0] > dis[0]:
                    mini = dis
        progress.append(mini[1])
        answer += mini[0]
    return answer
