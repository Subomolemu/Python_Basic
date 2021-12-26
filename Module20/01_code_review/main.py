def func(students_dict):
    lst = []
    cnt = 0
    for students_dict, inform in students_dict.items():
        lst.append(inform[1])
        cnt += len(students_dict[1])
    return lst, cnt


students = {
    ('Bob', 'Vazovski'): (23, ['biology, swimming']),
    ('Rob', 'Stepanov'): (24, ['math', 'computer games', 'running']),
    ('Alexander', 'Krug'): (22, ['languages', 'health food'])
}

print(f'Список пар "ID студента - Возраст": ')
for num, info in enumerate(students):
    num += 1
    print(f'{num}: {students[info][0]}')


lst_interest, total_age = func(students)

print('\nПолный список интересов всех студентов: ', end='')
for i in sum(lst_interest, []):
    print(f'{i}, ', end='')

print(f'\nОбщая длина всех фамилий студентов: {total_age}')
