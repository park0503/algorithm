def main():
    n = int(input())
    goal = []
    answer = []
    status = []
    current = 1
    result = True
    for i in range(n):
        goal.append(int(input()))
    for num in goal:
        if not status or status[-1] < num:
            if current > num:
                result = False
                print("NO")
                break
            for i in range(current, num+1):
                status.append(current)
                current += 1
                answer.append("+")
            answer.append("-")
            status.pop()
        elif num <= status[-1]:
            while status and num <= status[-1]:
                status.pop()
                answer.append("-")
    if result:
        for oper in answer:
            print(oper)


main()
