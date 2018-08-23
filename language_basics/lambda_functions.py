students = [
    ("Max", 5),
    ("Susi", 8),
    ("Jasmin", 4)
    ]

def students_key(item):
    return item[1]

print(students)
students.sort(key=students_key)                    # verwendet students_key als key function

students.sort(key=lambda student: student[1])      # lambda function inline

print(students)