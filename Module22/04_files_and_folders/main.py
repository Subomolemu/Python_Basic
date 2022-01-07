import os


def counting(path, size, total, file):
    for i_elem in os.listdir(path):
        next_path = os.path.join(path, i_elem)
        if os.path.isfile(next_path):
            file[0] += 1
            size[0] += os.path.getsize(next_path)
        elif os.path.isdir:
            total[0] += 1
            counting(next_path, size, total, file)
    return size, total, file


total_file = [0]
total_catalog = [0]
size_catalog = [0]
my_path = input('Введите путь до директории: ')

size_catalog, total_catalog, total_file = \
    counting(my_path, size_catalog, total_catalog, total_file)

print(f'Размер каталога (в Кб): {size_catalog[0] / 1024}\n'
      f'Количество подкаталогов: {total_catalog[0]}\n'
      f'Количество файлов: {total_file[0]}\n')
