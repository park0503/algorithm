import sys
F = [None] * 41
F[0] = {'num': 0, 'zero': 1, 'one': 0}
F[1] = {'num': 1, 'zero': 0, 'one': 1}


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    for i in range(n + 1):
        if F[i] is not None:
            continue
        else:
            data = {'num': F[i - 1]['num'] + F[i - 2]['num'],
                    'zero': F[i - 1]['zero'] + F[i - 2]['zero'],
                    'one': F[i - 1]['one'] + F[i - 2]['one']}
            F[i] = data
    print(F[n]['zero'], F[n]['one'])
