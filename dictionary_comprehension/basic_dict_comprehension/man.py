import random
name = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {student: random.randint(1, 100) for student in name}
print({student: score for (student, score) in student_score.items() if score >= 35})

# 4th line can also be written like these
# passed_student = {student: score for (student, score) in student_score.items() if score >= 35}
# print(passed_student)
