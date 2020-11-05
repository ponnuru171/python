student = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append([score, name])
student.sort()
grade = student[0][0]
for i in range(1, len(student)):
    if grade < student[i][0]:
        grade = student[i][0]
        break
for i in range(1, len(student)):
    if student[i][0] == grade:
        print(student[i][1])