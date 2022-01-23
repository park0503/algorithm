def main():
    n = int(input())
    goal = []
    answer = []
    current = []
    next = 1
    result = True
    for i in range(n):
        goal.append(int(input()))
    for num in goal:
        if not current or current[-1] < num:
            if next > num:
                result = False
                print("NO")
                break
            for i in range(next, num+1):
                current.append(next)
                next += 1
                answer.append("+")
            answer.append("-")
            current.pop()
        elif num <= current[-1]:
            while current and num <= current[-1]:
                current.pop()
                answer.append("-")
    if result:
        for oper in answer:
            print(oper)


main()
