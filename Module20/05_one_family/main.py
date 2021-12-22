dict_family = {
    ('Сидоров', 'Никита'): 25,
    ('Сидорова', 'Анна'): 28,
    ('Петров', 'Владислав'): 32,
    ('Петрова', 'Алена'): 30,
    ('Петров', 'Андрей'): 41,
    ('Иванов', 'Олег'): 39,
    ('Иванова', 'Анастасия'): 34,
    }

chose_surname = input('Введите фамилию: ').lower().title()

for f_n, age in dict_family.items():
    surname = f_n[0]
    if surname[:len(chose_surname)] == chose_surname:
        print(f'{f_n[0]} {f_n[1]}, {age} лет.')
    elif surname[0] == chose_surname[:len(surname[0])]:
        print(f'{f_n[0]} {f_n[1]}, {age} лет.')
