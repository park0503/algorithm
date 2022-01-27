import sys


def main():
    n = int(sys.stdin.readline())
    students = []
    ranking = []
    for i in range(n):
        student = list(map(int, sys.stdin.readline().split()))
        student.append(1)
        students.append(student)
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[i][0] < students[j][0] and students[i][1] < students[j][1]:
                students[i][2] += 1
            elif students[i][0] > students[j][0] and students[i][1] > students[j][1]:
                students[j][2] += 1
        ranking.append(str(students[i][2]))
    print(" ".join(ranking))


main()
