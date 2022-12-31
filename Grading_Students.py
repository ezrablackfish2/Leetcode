def gradingStudents(grades):
    answer = []
    b = 0
    for grade in grades:
        print(grade)
        if grade < 38:
            answer.append(grade)
        else:
            b = grade // 5
            b = b + 1
            if b * 5 - grade >= 3:
                answer.append(grade)
            else:
                c = b * 5
                answer.append(c)
    return answer


gradingStudents([74])
print(gradingStudents([65]))
