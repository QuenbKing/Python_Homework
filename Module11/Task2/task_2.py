from student import Student

print('Задача 2. Студенты\n')

students = []

for _ in range(10):
    name = input('Введите имя студента: ')
    surname = input('Введите фамилию студента: ')
    group = int(input('Введите номер группы студента: '))
    students.append(Student(name, surname, group))

sorted_students = sorted(students, key=lambda student: sum(student.estimations) / len(student.estimations))

for i_student in sorted_students:
    i_student.print_info()