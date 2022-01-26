import sys
import math
def cutTree():
    n, m = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))
    stock = 0
    next = 1
    trees.sort(reverse=True)
    while next < n:
        cutting = trees[next - 1] - trees[next]
        stock += cutting * next
        if stock == m:
            return trees[next]
        elif stock > m:
            return trees[next] + (stock - m) // next
        next += 1
    return trees[-1] - math.ceil((m - stock) / n)

print(cutTree())