import itertools
def solution(numbers):
    answer = ''
    candidates = []
    for candidate in list(itertools.permutations(numbers, len(numbers))):
        candidates.append(''.join(list(map(str, candidate))))
    candidates=sorted(candidates, reverse=True)
    answer = str(candidates[0])
    return answer