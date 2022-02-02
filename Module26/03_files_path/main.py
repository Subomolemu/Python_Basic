import os


def gen_files_path(path: str, find_path: str):
    for i_elem in os.listdir(path):
        try:
            next_path = os.path.join(path, i_elem)
            if i_elem == find_path:
                for i in os.listdir(next_path):
                    yield f'{os.path.join(next_path, i)}'
            else:
                if os.path.isdir(next_path):
                    for new_path in gen_files_path(next_path, find_path):
                        yield f'{os.path.join(next_path, new_path)}'
        except PermissionError:
            continue


start_path = os.path.abspath(os.path.join('/'))
my_path = 'Data'
found_path = gen_files_path(path=start_path, find_path=my_path)
print(found_path)
for my_path in found_path:
    print(my_path)
    