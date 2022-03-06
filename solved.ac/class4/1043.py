import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    known = set(map(int, sys.stdin.readline().split()[1:]))
    parties = []
    graph = {}
    visited = [False for _ in range(n + 1)]
    result = 0

    # 파티별 참여 인원 목록 및 진실 공유 graph 생성
    for _ in range(m):
        party = list(map(int, sys.stdin.readline().split()[1:]))
        for i, pi in enumerate(party):
            for pj in party[i + 1:]:
                if pi not in graph:
                    graph[pi] = set()
                graph[pi].add(pj)
                if pj not in graph:
                    graph[pj] = set()
                graph[pj].add(pi)
        parties.append(party)

    # 진실 공유 그래프 탐색
    for i in range(1, n + 1):
        if i in known and not visited[i]:
            stack = []
            c = i
            visited[i] = True
            while True:
                if c in graph:
                    for friend in graph[c]:
                        if not visited[friend]:
                            visited[friend] = True
                            known.add(friend)
                            stack.append(friend)
                if stack:
                    c = stack.pop()
                else:
                    break

    # 참여 가능 파티 탐색
    for party in parties:
        safe = True
        for p in party:
            if p in known:
                safe = False
                break
        if safe:
            result += 1

    print(result)


main()
