import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    things = {}
    dp = [[0, set()] for i in range(k + 1)]
    for i in range(n):
        w, v = map(int, sys.stdin.readline().split())
        things[i] = (w, v)
    dp[0][1] = set([i for i in range(n)])
    answer = 0
    for i in range(k):  # i : 현재 무게
        for j in dp[i][1]:  # j : 추가할 수 있는 물건의 index 번호
            nw = i + things[j][0]  # nw : 다음 무게, things[j][0] : 추가할 물건의 무게
            if nw > k:  # k : 최대 무게
                continue
            # nv: 다음 가치, things[j][1] : 추가할 물건의 가치
            nv = dp[i][0] + things[j][1]
            if nv < dp[nw][0]:  # dp[nw][0] 다음 무게의 기존 가치
                continue
            answer = max(answer, nv)
            dp[nw][0] = nv
            dp[nw][1] = set(dp[i][1])
            dp[nw][1].remove(j)
    print(answer)


main()
