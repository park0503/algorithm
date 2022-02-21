import sys
import heapq

def main():
    n = int(sys.stdin.readline())
    stack = []
    result = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x == 0:
            if not stack:
                result.append(x)
            else:
                result.append(-heapq.heappop(stack))
        else:
            heapq.heappush(stack, -x)
    for num in result:
        print(num)
main()