import sys


def main():
    n = int(sys.stdin.readline())
    costs = [[]]
    for _ in range(n):
        r, g, b = map(int, sys.stdin.readline().split())
        costs.append({'r': r, 'g': g, 'b': b})
    dp = [{}]
    dp.append({'r': costs[1]['r'], 'g': costs[1]['g'], 'b': costs[1]['b']})
    for i in range(2, n + 1):
        r = min(dp[i - 1]['g'] + costs[i]['r'], dp[i - 1]['b'] + costs[i]['r'])
        g = min(dp[i - 1]['r'] + costs[i]['g'], dp[i - 1]['b'] + costs[i]['g'])
        b = min(dp[i - 1]['r'] + costs[i]['b'], dp[i - 1]['g'] + costs[i]['b'])
        dp.append({'r': r, 'g': g, 'b': b})
    print(min(dp[n]['r'], dp[n]['g'], dp[n]['b']))


main()
