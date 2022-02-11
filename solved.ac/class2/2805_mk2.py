import sys
import math
def cutTree():
    n, m = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))
    trees.sort(reverse=True)
    mid = 0
    left = 0
    right = trees[0]
    while left > right:
        mid = (left + right) // 2
        stock = 0
        for tree in trees:
            if mid < tree:
                stock += tree - mid
        if stock < m:
            right = mid
        else:
            left = mid
    return mid
print(cutTree())