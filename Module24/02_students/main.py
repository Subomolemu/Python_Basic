import random
import student


student_list = []

student_1 = student.Student('Сергей Сергеевич', 1,
                            [random.randint(2, 5) for _ in range(5)])
student_2 = student.Student('Иван Иванович', 1,
                            [random.randint(2, 5) for _ in range(5)])
student_3 = student.Student('Петре Петрович', 1,
                            [random.randint(2, 5) for _ in range(5)])
student_4 = student.Student('Андрей Андреевич', 2,
                            [random.randint(2, 5) for _ in range(5)])
student_5 = student.Student('Анна Павловна', 2,
                            [random.randint(2, 5) for _ in range(5)])
student_6 = student.Student('Елена Александровна', 2,
                            [random.randint(2, 5) for _ in range(5)])
student_7 = student.Student('Ольга Владимировна', 3,
                            [random.randint(2, 5) for _ in range(5)])
student_8 = student.Student('Екатерина Григорьевна', 3,
                            [random.randint(2, 5) for _ in range(5)])
student_9 = student.Student('Татьяна Романовна', 3,
                            [random.randint(2, 5) for _ in range(5)])
student_10 = student.Student('Григорий Григорьевич', 3,
                             [random.randint(2, 5) for _ in range(5)])

student_list.append(student_1)
student_list.append(student_2)
student_list.append(student_3)
student_list.append(student_4)
student_list.append(student_5)
student_list.append(student_6)
student_list.append(student_7)
student_list.append(student_8)
student_list.append(student_9)
student_list.append(student_10)

student_list.sort(key=student.Student.sort_student)

for student in student_list:
    print(f'{student.info}. Средний балл: {student.sort_student()}.')
