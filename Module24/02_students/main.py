import random
import student


def sort_key(a):
    return a[1]


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

student_list.append([student_1.info, student_1.average_score()])
student_list.append([student_2.info, student_2.average_score()])
student_list.append([student_3.info, student_3.average_score()])
student_list.append([student_4.info, student_4.average_score()])
student_list.append([student_5.info, student_5.average_score()])
student_list.append([student_6.info, student_6.average_score()])
student_list.append([student_7.info, student_7.average_score()])
student_list.append([student_8.info, student_8.average_score()])
student_list.append([student_9.info, student_9.average_score()])
student_list.append([student_10.info, student_10.average_score()])

student_list.sort(key=sort_key)

for student in student_list:
    print(f'{student[0]}. Средний балл: {student[1]}.')
