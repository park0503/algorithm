def main():
    info = input()
    k, n = list(map(int, info.split()))
    lans = []
    for i in range(k):
        lans.append(input())
    print(lans)
