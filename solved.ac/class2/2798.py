import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
cards.sort()
length = len(cards)
minimum = 0
end_token = 0
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            hab = cards[i] + cards[j] + cards[k]
            if m == hab:
                minimum = hab
                end_token = 1
                break
            elif hab < m:
                if m - hab < m - minimum:
                    minimum = hab
                    continue
            else:
                break
        if end_token == 1:
            break
    if end_token == 1:
        break
print(minimum)