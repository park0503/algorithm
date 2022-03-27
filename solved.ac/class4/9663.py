N = int(input())
result = 0
horis = set()
sumas = set()
subas = set()


def checkcheck(depth):
    global result
    for j in range(N):
        if j in horis:
            continue
        suma = depth - 1 + j
        suba = depth - 1 - j
        if suma in sumas or suba in subas:
            continue
        if depth == 1:
            result += 1
            continue
        horis.add(j)
        sumas.add(suma)
        subas.add(suba)
        checkcheck(depth - 1)
        horis.remove(j)
        sumas.remove(suma)
        subas.remove(suba)


checkcheck(N)

print(result)
