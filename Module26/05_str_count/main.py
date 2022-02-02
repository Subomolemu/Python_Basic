import os


def total_str(path):
    count = 0
    for i_elem in os.listdir(path):
        new_path = os.path.join(path, i_elem)
        
        if i_elem.endswith('.py'):

            with open(f'{new_path}', 'r', encoding='utf-8') as main:
                
                for string in main:
                    if string.strip() == '':
                        continue
                    else:
                        if '#' in string:
                            continue
                        else:
                            count += 1
                yield f'В файле {new_path} {count} строк кода'
        elif os.path.isdir(new_path):
            for see_path in total_str(new_path):
                yield see_path


find_dir = os.path.abspath('..')
start_count = total_str(find_dir)
for i in start_count:
    print(i)
# комментарий
