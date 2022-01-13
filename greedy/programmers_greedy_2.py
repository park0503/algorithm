def solution(name):
    answer = 0
    current = 0
    name = list(name)
    size = len(name)
    possible = list(map(lambda x: False if x == 'A' else True, name))
    while True:
        if possible[current]:
            gap = abs(ord(name[current]) - ord('A'))
            gap = 26 - gap if gap > 13 else gap
            answer += gap
            possible[current] = False
        temp = []
        for tf in range(size):
            if possible[tf]:
                dis = abs(tf - current)
                dis = size - dis if dis > size / 2 else dis
                temp.append((dis, tf))
        if not temp:
            break
        next = min(temp, key=lambda x: x[0])
        answer += next[0]
        current = next[1]
    return answer
