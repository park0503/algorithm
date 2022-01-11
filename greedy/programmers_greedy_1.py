def solution(n, lost, reserve):
    answer = 0
    students = [1 for i in range(n)]
    for it in reserve:
        students[it - 1] += 1
    for it in lost:
        students[it - 1] -= 1
    for i in range(n):
        if students[i] == 0:
            if i > 0 and students[i-1] == 2:
                students[i] = 1
                students[i-1] = 1
            elif i < n - 1 and students[i+1] == 2:
                students[i] = 1
                students[i+1] = 1
    answer = n - students.count(0)
    return answer