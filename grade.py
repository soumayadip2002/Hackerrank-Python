n = int(input("enter the length: "))
student_record = []
for i in range(n):
    name = input("Enter name: ")
    Score = float(input("Enter Score: "))
    student_record.append([name, Score])

sorted_score = sorted(list(set(x[1] for x in student_record)))

second_lowest = sorted_score[1]

final_result = []

for student in student_record:
    if(second_lowest==student[1]):
        print(student[1])
        final_result.append(student[0])

for student in sorted(final_result):
    print(student)