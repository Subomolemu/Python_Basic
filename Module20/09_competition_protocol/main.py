def append_final_score():
    max_score = 0
    name_max_scores = ''
    for i_name, i_scores in date.items():
        if int(i_scores) > max_score:
            max_score = int(i_scores)
            name_max_scores = i_name

    if name_max_scores != '':
        date.pop(name_max_scores)
    else:
        return final_dict

    final_dict[name_max_scores] = max_score

    if len(final_dict) == 3:
        return final_dict
    else:
        append_final_score()


total_records = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя): ')
date = {}

for i_record in range(total_records):
    scores, name = input(f'{i_record + 1} запись: ').strip().split()

    if name not in date.keys():
        date[name] = int(scores)
    elif name in date.keys() and date[name] < int(scores):
        date.pop(name)
        date[name] = scores

final_dict = {}
append_final_score()

print('\nИтоги соревнований:')

for i, name in enumerate(final_dict):
    print(f'{i + 1} место: {name} ({final_dict[name]} ')
    
print('...')
